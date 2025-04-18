"""
依赖注入
"""

from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from taoist.core.config import settings
from taoist.core.db import engine
from taoist.core.models import TokenPayload, User


def get_db():
    with Session(engine) as session:
        yield session


oauth2_scheme = OAuth2PasswordBearer(f"{settings.app_prefix}/user/login")

SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(oauth2_scheme)]


def current_user(session: SessionDep, token: TokenDep):
    try:
        payload = jwt.decode(
            token, settings.app_secret, algorithms=[settings.app_algorithm]
        )
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(current_user)]


def current_active_user(current_user: CurrentUser):
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
