from pydantic import BaseModel, Field, EmailStr, ConfigDict

class CatModel(BaseModel):
    id: int
    name: str
    owner: str | None = Field(max_length = 20) #строка или Нон, максимальная длинна 20
    old: int = Field(ge = 0, le = 20) #число от 0 до 20 включительно
    email: EmailStr #тип почтового адреса

    model_config = ConfigDict(extra = 'forbid') #если в схеме есть лишнее данные, выдаст ошибку