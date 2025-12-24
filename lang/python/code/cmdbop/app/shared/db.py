"""
数据库连接
"""
import typing
from datetime import datetime, timezone
from contextlib import asynccontextmanager

import sqlalchemy as sa
import sqlalchemy.ext.asyncio as sasync
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.sql import func
from sqlalchemy.orm import selectinload, joinedload
from fastapi import Request
from pydantic import BaseModel


# 类型变量定义
ModelType = typing.TypeVar("ModelType")
CreateSchemaType = typing.TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = typing.TypeVar("UpdateSchemaType", bound=BaseModel)
SchemaType = typing.TypeVar("SchemaType", bound=BaseModel)


class Config:
    """
    数据库配置类
    """
    def __init__(
        self,
        database_url: str,
        pool_size: int = 20,
        max_overflow: int = 0,
        pool_pre_ping: bool = True,
        pool_recycle: int = 1800,
        echo: bool = False,
        hide_parameters: bool = True,
        **kwargs
    ):
         # 保存原始URL用于判断
        # original_url = database_url
        
        # 检查并转换同步驱动为异步驱动
        if database_url.startswith("sqlite://"):
            database_url = database_url.replace("sqlite://", "sqlite+aiosqlite://", 1)
        elif database_url.startswith("postgresql://"):
            database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        elif database_url.startswith("mysql://"):
            database_url = database_url.replace("mysql://", "mysql+aiomysql://", 1)
        # 如果已经是异步驱动，直接使用
        elif database_url.startswith("sqlite+aiosqlite://") or \
            database_url.startswith("postgresql+asyncpg://") or \
            database_url.startswith("mysql+aiomysql://"):
            # 已经是异步驱动，无需转换
            pass
        else:
            raise ValueError("Unsupported database type. Supported types are SQLite, PostgreSQL, and MySQL.")
        
        self.database_url = database_url
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.pool_pre_ping = pool_pre_ping
        self.pool_recycle = pool_recycle
        self.echo = echo
        self.hide_parameters = hide_parameters
        self.kwargs = kwargs


class AsyncEngineFactory:
    """
    异步数据库引擎工厂
    """

    @staticmethod
    def create_engine(config: Config) -> sasync.AsyncEngine:
        return sasync.create_async_engine(
            config.database_url,
            pool_size=config.pool_size,
            max_overflow=config.max_overflow,
            pool_pre_ping=config.pool_pre_ping,
            pool_recycle=config.pool_recycle,
            echo=config.echo,
            hide_parameters=config.hide_parameters,
            **config.kwargs
        )


class AsyncSessionManager:
    """异步数据库会话管理器"""
    def __init__(self):
        self._engine: typing.Optional[sasync.AsyncEngine] = None
        self._session_factory: typing.Optional[sasync.async_sessionmaker] = None
        
    def init(self, engine: sasync.AsyncEngine):
        self._engine = engine
        self._session_factory = sasync.async_sessionmaker(
            engine,
            class_=sasync.AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False
        )

    async def get_db(self) -> typing.AsyncGenerator[sasync.AsyncSession, None]:
        """获取数据库会话"""
        if self._session_factory is None:
            raise RuntimeError("Database session factory is not initialized.")
        
        async with self._session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    @asynccontextmanager
    async def session_scope(self) -> typing.AsyncGenerator[sasync.AsyncSession, None]:
        """提供异步事务作用域"""
        async with self._session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    async def close(self):
        """关闭数据库引擎"""
        if self._engine:
            await self._engine.dispose()


class Base(DeclarativeBase, sasync.AsyncAttrs):
    """异步模型基础类"""

    @declared_attr
    def __tablename__(cls):
        """自动生成表名（类名转小写复数）"""
        import re
        # 将驼峰命名转换为下划线命名
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
        # 添加复数形式（简单处理）
        if not name.endswith('s'):
            name += 's'
        return name
    
    id = sa.Column(sa.Integer, primary_key=True, index=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = sa.Column(
        sa.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False
    )
    
    def to_dict(self, exclude: typing.List[str] = None) -> typing.Dict:
        """将模型转换为字典"""
        if exclude is None:
            exclude = []
            
        result = {}
        for column in self.__table__.columns:
            if column.name not in exclude:
                value = getattr(self, column.name)
                # 处理datetime对象
                if isinstance(value, datetime):
                    value = value.isoformat()
                result[column.name] = value
        return result


class AsyncCRUDBase(typing.Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """异步CRUD基类"""
    def __init__(self, model: typing.Type[ModelType]):
        """
        CRUD对象初始化
        :param model: SQLAlchemy模型类
        """
        self.model = model

    async def get(self, db: sasync.AsyncSession, id: typing.Any) -> typing.Optional[ModelType]:
        """根据ID获取单个记录"""
        try:
            stmt = sa.select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise f"Error getting record by id {id}: {e}"

    async def get_by_ids(self, db: sasync.AsyncSession, ids: typing.List[typing.Any]) -> typing.List[ModelType]:
        """根据多个ID获取记录列表"""
        try:
            if not ids:
                return []
            stmt = sa.select(self.model).where(self.model.id.in_(ids))
            result = await db.execute(stmt)
            return list(result.scalars())
        except SQLAlchemyError as e:
            raise f"Error getting records by ids: {e}"
        
    async def get_multi(
        self, 
        db: sasync.AsyncSession, 
        *, 
        skip: int = 0, 
        limit: int = 100, 
        filters: typing.Optional[list] = None,
        order_by: typing.Optional[list] = None,
        load_relations: typing.Optional[list] = None,
    ) -> typing.List[ModelType]:
        """获取多条记录"""
        try:
            stmt = sa.select(self.model)
            # 应用过滤条件
            if filters:
                for condition in filters:
                    stmt = stmt.where(condition)

            # 预加载关联关系
            if load_relations:
                for relation in load_relations:
                    stmt = stmt.options(selectinload(relation))
                    
            # 应用排序条件
            if order_by:
                stmt = stmt.order_by(*order_by)

            # 应用分页
            stmt = stmt.offset(skip).limit(limit)
            result = await db.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            raise f"Error getting multiple records: {e}"
        
    async def get_one(
        self,
        db: sasync.AsyncSession,
        *,
        filters: typing.Optional[list] = None,
        load_relations: typing.Optional[list] = None,
    ) -> typing.Optional[ModelType]:
        """获取单条记录"""
        try:
            stmt = sa.select(self.model)
            # 应用过滤条件
            if filters:
                for condition in filters:
                    stmt = stmt.where(condition)

            # 预加载关联关系
            if load_relations:
                for relation in load_relations:
                    stmt = stmt.options(selectinload(getattr(self.model, relation)))

            stmt = stmt.limit(1)
            result = await db.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise f"Error getting single record: {e}"
        
    async def create(
        self,
        db: sasync.AsyncSession,
        *,
        obj_in: CreateSchemaType
    ) -> ModelType:
        """创建新记录"""
        try:
            obj_in_data = obj_in.model_dump() if hasattr(obj_in, 'model_dump') else obj_in.dict()
            db_obj = self.model(**obj_in_data)  # type: ignore
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj
        except IntegrityError as e:
            await db.rollback()
            raise f"Integrity error creating record: {e}"
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Error creating record: {e}"
        
    async def create_bulk(
        self,
        db: sasync.AsyncSession,
        *,
        objs_in: list[CreateSchemaType],
        chunk_size: int = 100
    ) -> list[ModelType]:
        """批量创建记录"""
        try:
            db_objs = []
            for i, obj_in in enumerate(objs_in):
                obj_in_data = obj_in.model_dump() if hasattr(obj_in, 'model_dump') else obj_in.dict()
                db_obj = self.model(**obj_in_data)  # type: ignore
                db.add(db_obj)
                db_objs.append(db_obj)
                
                if (i + 1) % chunk_size == 0:
                    await db.flush()
                
            await db.commit()

            # 刷新所有对象
            for db_obj in db_objs:
                await db.refresh(db_obj)
            return db_objs
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Integrity error creating records in bulk: {e}"
        
    async def update(
        self,
        db: sasync.AsyncSession,
        *,
        db_obj: ModelType,
        obj_in: typing.Union[UpdateSchemaType, typing.Dict[str, typing.Any]]
    ) -> ModelType:
        """更新记录"""
        try:
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True) if hasattr(obj_in, 'model_dump') else obj_in.dict(exclude_unset=True)
            for field, value in update_data.items():
                if hasattr(db_obj, field):
                    setattr(db_obj, field, value)
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Error updating record: {e}"
        
    async def update_filter(
        self,
        db: sasync.AsyncSession,
        *,
        filters: list,
        update_data: typing.Dict[str, typing.Any]
    ) -> int:
        """根据条件更新多条记录"""
        try:
            stmt = sa.update(self.model).where(*filters).values(**update_data)
            result = await db.execute(stmt)
            await db.commit()
            return result.rowcount
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Error updating records by filter: {e}"

    async def delete(self, db: sasync.AsyncSession, *, id: int) -> bool:
        """删除记录"""
        try:
            stmt = sa.select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            obj = result.scalar_one_or_none()
            
            if obj:
                await db.delete(obj)
                await db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Error deleting record with id {id}: {e}"

    async def delete_by_filter(self, db: sasync.AsyncSession, *, filters: list) -> int:
        """根据条件删除多个记录"""
        try:
            stmt = sa.delete(self.model).where(*filters)
            result = await db.execute(stmt)
            await db.commit()
            return result.rowcount
        except SQLAlchemyError as e:
            await db.rollback()
            raise f"Error deleting records by filter: {e}"

    async def count(self, db: sasync.AsyncSession, filters: typing.Optional[list] = None) -> int:
        """统计记录数量"""
        try:
            stmt = sa.select(func.count()).select_from(self.model)
            if filters:
                for filter_condition in filters:
                    stmt = stmt.where(filter_condition)
            result = await db.execute(stmt)
            return result.scalar_one()
        except SQLAlchemyError as e:
            raise f"Error counting records: {e}"

    async def exists(self, db: sasync.AsyncSession, *, filters: list) -> bool:
        """检查记录是否存在"""
        try:
            stmt = sa.select(self.model.id).where(*filters).limit(1)
            result = await db.execute(stmt)
            return result.scalar_one_or_none() is not None
        except SQLAlchemyError as e:
            raise f"Error checking existence of records: {e}"
        
    async def paginate(
        self,
        db: sasync.AsyncSession,
        *,
        page: int = 1,
        per_page: int = 20,
        filters: typing.Optional[list] = None,
        order_by: typing.Optional[list] = None,
        load_relationships: typing.Optional[list] = None
    ) -> typing.Dict[str, typing.Any]:
        """分页查询"""
        try:
            # 计算偏移量
            skip = (page - 1) * per_page
            
            # 获取数据
            items = await self.get_multi(
                db,
                skip=skip,
                limit=per_page,
                filters=filters,
                order_by=order_by,
                load_relationships=load_relationships
            )
            
            # 获取总数
            total = await self.count(db, filters=filters)
            
            # 计算总页数
            total_pages = (total + per_page - 1) // per_page if total > 0 else 0
            
            return {
                "items": items,
                "total": total,
                "page": page,
                "per_page": per_page,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1
            }
        except SQLAlchemyError as e:
            raise f"Error paginating records: {e}"


class AsyncService:
    """异步数据库服务类(单例)"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.session_manager = AsyncSessionManager()
            self._initialized = True
    
    async def init_app(self, config: Config):
        """初始化应用"""
        engine = AsyncEngineFactory.create_engine(config)
        self.session_manager.init(engine)
        
        # 异步创建所有表
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return self
    
    async def get_db(self):
        """获取数据库会话"""
        async for session in self.session_manager.get_db():
            yield session
    
    def get_session_scope(self):
        """获取会话作用域上下文管理器"""
        return self.session_manager.session_scope
    
    async def close(self):
        """关闭数据库连接"""
        await self.session_manager.close()


# FastAPI依赖项
async def get(request: Request) -> typing.AsyncGenerator[sasync.AsyncSession, None]:
    """获取数据库会话(FastAPI依赖)"""
    db_service: AsyncService = request.app.state.db_service
    async for session in db_service.get_db():
        yield session


# 异步事务装饰器
def async_transactional(func):
    """异步事务装饰器"""
    async def wrapper(*args, **kwargs):
        # 查找数据库会话
        db = None
        for arg in args:
            if isinstance(arg, sasync.AsyncSession):
                db = arg
                break
        
        if db is None:
            for value in kwargs.values():
                if isinstance(value, sasync.AsyncSession):
                    db = value
                    break
        
        if db is None:
            raise ValueError("No AsyncSession found in arguments")
        
        try:
            result = await func(*args, **kwargs)
            await db.commit()
            return result
        except Exception as e:
            await db.rollback()
            raise f"Transaction error in {func.__name__}: {e}"
    
    return wrapper


