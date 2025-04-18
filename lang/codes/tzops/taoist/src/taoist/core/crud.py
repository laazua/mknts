from sqlmodel import Session, select

from taoist.core.models import User
from taoist.core.security import verify_password


def get_user_by_name(*, session: Session, name: str):
    statement = select(User).where(User.name == name)
    session_user = session.exec(statement).first()
    return session_user


def authenticate(*, session: Session, name: str, password: str):
    db_user = get_user_by_name(session=session, name=name)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
