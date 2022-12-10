from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from books.models import BookModel
from books.schemas import BookCreate , Book
from database import SessionLocal, engine
from fastapi_crudrouter import SQLAlchemyCRUDRouter





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = SQLAlchemyCRUDRouter(
    schema=Book,
    create_schema=BookCreate,
    db_model=BookModel,
    # dependencies=[Depends(token_auth)],
    # update_schema=UserCreate
    db=get_db,
    # delete_all_route=False,
    prefix='book'
)
