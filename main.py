from fastapi import Depends, FastAPI, HTTPException ,  Request
import users.models as models
import permissions.models as permission_model 
from users.routes import router as user_router
from permissions.routes import router as permission_router
from roles.routes import router as roles_router
from role_users.routes import router as role_users_router
from permission_roles.routes import router as permission_roles_router
from database import SessionLocal, engine , session , Base
from auth.login import router as login_router
from auth.register import router as register_router
import time
import os 
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
# permission_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router, tags=["login"], prefix="/api/v1.0/login")
app.include_router(register_router, tags=["register"], prefix="/api/v1.0/register")
app.include_router(user_router, tags=["Users"], prefix="/api/v1.0/users")
app.include_router(permission_router, tags=["Permissions"], prefix="/api/v1.0/permissions")
app.include_router(roles_router, tags=["Roles"], prefix="/api/v1.0/roles")
app.include_router(permission_roles_router, tags=["Permission_role"], prefix="/api/v1.0/permission_role")
app.include_router(role_users_router, tags=["Role_users"], prefix="/api/v1.0/role_users")

from sqlalchemy_seed import (
    create_table,
    drop_table,
    load_fixtures,
    load_fixture_files,
)


# def main():
#     path =  os.getcwd() 
#     fixtures = load_fixture_files(path, ['seeds.yaml'])
#     load_fixtures(session, fixtures)

# main()
