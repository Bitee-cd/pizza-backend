from pydantic import BaseModel
from typing import Optional



class SignUpModel(BaseModel):
    id:Optional[int]
    username :str
    email:str
    password :str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='da3a7111c1b733d9c2e094ea306223a799e88f8474511bdad26e1694bab85c8b'


class LoginModel(BaseModel):
    username:str
    password:str


class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]

    class Config:
        orm_mode=True
        schema_extra={
            "extra":{
                "quantity":2,
                "pizza_size":"large"
            }
        }