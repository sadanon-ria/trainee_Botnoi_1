from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    age: str
    gender: str

class data(BaseModel):
    age: str
    gender: str

class UserSchema(BaseModel):
    name:str
    email: str
    password: str

class UserLoginSchema(BaseModel):
    email: str
    password: str

