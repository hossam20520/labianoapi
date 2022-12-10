
from sqlalchemy.orm import Session
from permissions.models import PermissionModel
from permissions.schemas import PermissionCreate , Permission
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from global_schemas import ResponseModel



def get_permissions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PermissionModel).offset(skip).limit(limit).all()


def create_permission(db: Session, permission:Permission):
    try:
        db_permission  = PermissionModel(**permission.dict())
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Permission already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_permission


def delete_all_permission(db: Session):
    db.query(PermissionModel).delete()
    db.commit()
    return []


def get_permission(db: Session, permission_id: int):
    return db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()


def get_permission_by_email(db: Session, email: str):
    return db.query(PermissionModel).filter(PermissionModel.email == email).first()

def update_permission(db: Session , permission: dict , id: int):
   db.query(PermissionModel).filter(PermissionModel.id == id).update(dict(permission), synchronize_session = False)
   db.commit()
   return permission


def delete_permission(db: Session , id:int):
    db_model = db.query(PermissionModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Permission not found" , True , 404 , {}))


def seed_permissions(db:Session):
    permissions = [
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"1","title":"read__users","label":"read__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"2","title":"create__user","label":"create__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"3","title":"delete__users","label":"delete__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"4","title":"show__user","label":"show__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"5","title":"update__user","label":"update__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"6","title":"delete__user","label":"delete__user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"7","title":"read__permissions","label":"read__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"8","title":"create__permission","label":"create__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"9","title":"delete__permissions","label":"delete__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"10","title":"show__permission","label":"show__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"11","title":"update__permission","label":"update__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"12","title":"delete__permission","label":"delete__permission"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"13","title":"read__role_users","label":"read__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"14","title":"create__role_user","label":"create__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"15","title":"delete__role_users","label":"delete__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"16","title":"show__role_user","label":"show__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"17","title":"update__role_user","label":"update__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"18","title":"delete__role_user","label":"delete__role_user"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"19","title":"read__roles","label":"read__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"20","title":"create__role","label":"create__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"21","title":"delete__roles","label":"delete__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"22","title":"show__role","label":"show__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"23","title":"update__role","label":"update__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"24","title":"delete__role","label":"delete__role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"25","title":"read__permission_roles","label":"read__permission_role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"26","title":"create__permission_role","label":"create__permission_role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"27","title":"delete__permission_roles","label":"delete__permission_role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"28","title":"show__permission_role","label":"show__permission_role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"29","title":"update__permission_role","label":"update__permission_role"},
{"created_at":"2022-12-10 10:41:22","updated_at":"2022-12-10 10:41:22","id":"30","title":"delete__permission_role","label":"delete__permission_role"}
]

    for items in permissions:
        try:
            db_permission  = PermissionModel(**items)
            db.add(db_permission)

        except IntegrityError:
            db.rollback()
            raise HTTPException(422, ResponseModel([] , "Permission already exist" , False , 422 , {"error":"Already exists"})) from None
    db.commit()             
    db.refresh(db_permission)
    raise HTTPException(200, ResponseModel([] , "Success Seed" , False , 200 , {})) from None
