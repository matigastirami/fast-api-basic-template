from dataclasses import dataclass
from fastapi import APIRouter, Depends
from sqlmodel import Session

from config.database import get_db
from api.models.user_model import User

@dataclass
class UserPayload:
    username: str
    password: str

user_router = APIRouter(
    prefix='/users',
    tags=['users']
)

@user_router.get('/')
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@user_router.post('/')
async def create_user(payload: UserPayload, db: Session = Depends(get_db)):
    new_user = User(
        username=payload.username,
        password=payload.password
    )

    db.add(new_user)
    db.commit()
    return {
        'success': True,
        'message': 'Successfully created user'
    }
