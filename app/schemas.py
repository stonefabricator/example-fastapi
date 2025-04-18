from pydantic import BaseModel,ConfigDict, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id: int
    owner: UserOut  # return a pydantic model type
    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post: Post
    votes: int
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token:str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore