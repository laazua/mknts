import asyncio
import logging
from typing import List, Callable, Any
from concurrent.futures import ThreadPoolExecutor
from .exceptions import PoolError


logger = logging.getLogger(__name__)


class CoroutinePool:
    """
    协程池实现
    """
    
    def __init__(self, max_workers: int = 100, queue_size: int = 1000):
        """
        初始化协程池
        
        Args:
            max_workers: 最大工作协程数
            queue_size: 任务队列大小
        """
        self.max_workers = max_workers
        self.queue_size = queue_size
        self._task_queue = asyncio.Queue(maxsize=queue_size)
        self._workers: List[asyncio.Task] = []
        self._is_running = False
        self._thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        
    async def start(self):
        """启动协程池"""
        if self._is_running:
            return
            
        self._is_running = True
        # 创建工作协程
        for i in range(self.max_workers):
            worker = asyncio.create_task(self._worker_loop(), name=f"worker-{i}")
            self._workers.append(worker)
            
        logger.info(f"CoroutinePool started with {self.max_workers} workers")
        
    async def stop(self, timeout: float = 30):
        """停止协程池"""
        if not self._is_running:
            return
            
        self._is_running = False
        
        # 等待所有任务完成
        await self._task_queue.join()
        
        # 取消所有工作协程
        for worker in self._workers:
            worker.cancel()
            
        # 等待工作协程结束
        await asyncio.gather(*self._workers, return_exceptions=True)
        self._workers.clear()
        self._thread_pool.shutdown(wait=True)
        
        logger.info("CoroutinePool stopped")
        
    async def submit(self, func: Callable, *args, **kwargs) -> Any:
        """
        提交任务到协程池
        
        Args:
            func: 要执行的函数
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            任务执行结果
        """
        if not self._is_running:
            raise PoolError("CoroutinePool is not running")
            
        future = asyncio.Future()
        await self._task_queue.put((func, args, kwargs, future))
        return await future
        
    async def _worker_loop(self):
        """工作协程循环"""
        while self._is_running:
            try:
                func, args, kwargs, future = await self._task_queue.get()
                
                try:
                    # 如果是协程函数，直接await
                    if asyncio.iscoroutinefunction(func):
                        result = await func(*args, **kwargs)
                    else:
                        # 普通函数在线程池中执行
                        loop = asyncio.get_event_loop()
                        result = await loop.run_in_executor(
                            self._thread_pool, func, *args, **kwargs
                        )
                    future.set_result(result)
                    
                except Exception as e:
                    future.set_exception(e)
                    
                finally:
                    self._task_queue.task_done()
                    
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Worker error: {e}")
                
    @property
    def pending_tasks(self) -> int:
        """获取待处理任务数量"""
        return self._task_queue.qsize()
        
    @property
    def active_workers(self) -> int:
        """获取活跃工作协程数量"""
        return sum(1 for w in self._workers if not w.done())