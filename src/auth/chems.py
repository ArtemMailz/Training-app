from pydantic import BaseModel

class UserLoginShema(BaseModel):
    username: str
    password: str