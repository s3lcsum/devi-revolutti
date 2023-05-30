from sqlalchemy import Column , String, Date

from db.session import DBBase


class UserModel(DBBase):
    __tablename__ = "users"

    username = Column(String(64), primary_key=True, unique=True, index=True)
    dateOfBirth = Column(Date)
