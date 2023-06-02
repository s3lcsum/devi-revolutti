import re

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
        username: str,
        db: Session = Depends(get_db)
):
    # Get the user from the database based on the username
    db_user = crud.user.get_by_name(db, username=username)

    if not db_user:
        # User not found, raise 404 HTTPException
        raise HTTPException(status_code=404)

    # Calculate the number of days until the user's next birthday
    delta = days_until_next(db_user.dateOfBirth)

    if delta.days == 0:
        # User's birthday is today
        return {
            'message': f"Hello, {username}! Happy birthday!"
        }

    # User's birthday is in the future
    return {
        'message': f"Hello, {username}! Your birthday is in {delta.days} day(s)"
    }


@router.put("/{username}", status_code=204, name="user:update")
async def update(
        username: str,
        user_schema: UserCreateSchema,
        db: Session = Depends(get_db)
):
    # Validate that the username contains only letters
    if not re.match(r"^[a-zA-Z]+$", username):
        # Invalid username, raise 422 HTTPException
        raise HTTPException(status_code=422)

    # Get the user from the database based on the username
    db_user = crud.user.get_by_name(db, username=username)

    if db_user:
        # User already exists, update their date of birth
        db_user.dateOfBirth = user_schema.dateOfBirth
    else:
        # User doesn't exist, create a new user
        db_user = UserModel(username=username, dateOfBirth=user_schema.dateOfBirth)

    # Create or update the user in the database
    crud.user.create_or_update(db, db_obj=db_user)