from typing import List, Optional
from sqlalchemy.orm import Session
from models.user import UserModel


def get_by_name(db_session: Session, *, username: str) -> Optional[UserModel]:
    # Query the database to retrieve a user by their username
    return db_session.query(UserModel).filter(UserModel.username == username).first()


def create_or_update(db_session: Session, *, db_obj: UserModel) -> UserModel:
    # Add the user object to the session, commit the changes, and refresh the object
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj
