from typing import List, Optional

from fastapi.encoders import jsonable_encoder

from schemas.user import UserCreateSchema, UserUpdateSchema, UserSchema

from sqlalchemy.orm import Session

from models.user import UserModel


def get_by_name(db_session: Session, *, username: str) -> Optional[UserModel]:
    return db_session.query(UserModel).filter(UserModel.username == username).first()


def create_or_update(db_session: Session, *, db_obj: UserModel) -> UserModel:
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj
