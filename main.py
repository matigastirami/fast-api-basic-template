from fastapi import Depends, FastAPI
from sqlmodel import Session

from config.database import get_db
from api.models.user_model import User

app = FastAPI()

@app.get('/')
def greet():
    return {'message': 'Hello world!'}

@app.get('/users')
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
