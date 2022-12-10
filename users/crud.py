from sqlalchemy.orm import Session
from users.models import UserModel 
from users.schemas import UserCreate , User
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from global_schemas import ResponseModel

from sqlalchemy.sql import func



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user:User):
    try:
        db_user  = UserModel(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "User already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_user


def delete_all_user(db: Session):
    db.query(UserModel).delete()
    db.commit()
    return []


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def update_user(db: Session , user: dict , id: int):
   db.query(UserModel).filter(UserModel.id == id).update(dict(user), synchronize_session = False)
   db.commit()
   return user


def delete_user(db: Session , id:int):
    db_model = db.query(UserModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "User not found" , True , 404 , {}))




def create_user_seeds(db: Session):
    users = [
{"created_at":"2022-12-10 10:40:00","updated_at":"2022-12-10 10:47:14","id":"1","first_name":"string","last_name":"string","username":"strding","email":"stringd","hashed_password":"string","is_active":True,"role_id":"1"},
{"created_at":"2022-12-10 10:40:00","updated_at":"2022-12-10 10:40:00","id":"2","first_name":"Eslam","last_name":"mohamed","username":"eslam2020","email":"eslam@gmail.com","hashed_password":"$2b$12$I0TLrFYjkSTcXlutReGL1.0rQS2BywxpDSgXpZbzlmTtFj9aXMJVK","is_active":True,"role_id":"2"},
{"created_at":"2022-12-10 10:40:00","updated_at":"2022-12-10 10:40:00","id":"3","first_name":"Ahmed","last_name":"Hassan","username":"ahmed","email":"ahmed@gmail.com","hashed_password":"$2b$12$I0TLrFYjkSTcXlutReGL1.0rQS2BywxpDSgXpZbzlmTtFj9aXMJVK","is_active":True},
{"created_at":"2022-12-10 10:44:34","updated_at":"2022-12-10 10:44:34","id":"4","first_name":"string","last_name":"string","username":"string","email":"string","hashed_password":"string","is_active":True}
]
    for items in users:
        try:
            db_user  = UserModel(**items)
            db.add(db_user)

        except IntegrityError:
            db.rollback()
            raise HTTPException(422, ResponseModel([] , "User already exist" , False , 422 , {"error":"Already exists"})) from None
    db.commit()             
    db.refresh(db_user)
    raise HTTPException(200, ResponseModel([] , "Success Seed" , False , 200 , {})) from None
