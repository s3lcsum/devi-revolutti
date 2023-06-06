from datetime import date, datetime
from pydantic import BaseModel, types, validator


# =================================================
# Base classes should only be used to inherit from.
# =================================================

class UserBaseSchema(BaseModel):
    dateOfBirth: types.date

    @validator("dateOfBirth")
    def validate_date(cls, v):
        if not v < date.today():
            raise ValueError("You're from the future!")

        return v


# Properties to receive via API on creation
class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdateSchema(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema):
    username: str

    class Config:
        orm_mode = True
