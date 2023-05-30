from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import crud.user
from models.user import UserModel
from schemas.user import UserCreateSchema
from utils.get_db import get_db
from utils.datedelta import days_until_next

router = APIRouter()


@router.get("/{username}", status_code=200, name="user:get")
async def get(
        *,
        username: str,
        db: Session = Depends(get_db)
):
    db_user = crud.user.get_by_name(db, username=username)

    if not db_user:
        return HTTPException(status_code=404)

    delta = days_until_next(db_user.dateOfBirth)

    if delta.days == 0:
        return {
            'message': "Hello, {username}! Happy birthday!"
        }

    return {
        'message': "Hello, {username}! Your birthday is in {n} day(s)"
        .format(username=db_user.username, n=delta.days)
    }


@router.put("/{username}", status_code=204, name="user:update")
async def update(
        *,
        username: str,
        user_schema: UserCreateSchema,
        db: Session = Depends(get_db)
):
    db_user = crud.user.get_by_name(db, username=username)

    if db_user:
        db_user.dateOfBirth = user_schema.dateOfBirth
    else:
        db_user = UserModel(username=username, dateOfBirth=user_schema.dateOfBirth)

    crud.user.create_or_update(db, db_obj=db_user)
