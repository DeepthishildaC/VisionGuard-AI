from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str
    role_id: int


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True