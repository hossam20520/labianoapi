from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr




class BookCreate(BaseModel):
    user_id:int
    title:str
    author:str

    


class Book(BookCreate):
    id: int


    class Config:
        orm_mode = True



# class UserBase(BaseModel):
#     first_name:  str
#     last_name: str
#     username: str
#     email: EmailStr
    
    


# class UserCreate(UserBase):
#     password: str

# class UpdateUser(UserBase):
#     first_name: Optional[str]
#     last_name: Optional[str]
#     username: Optional[str]
#     email: Optional[EmailStr]
         

        
# class User(UserBase):
#     id: int
#     is_active: bool
    

#     class Config:
#         orm_mode = True
        
        
# def  ResponseModel(data , message, status, error):
# 	return  {
# 	"data": data ,
# 	"message":message,
# 	"status":status,
# 	"error":error
# 	}
