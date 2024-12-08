from pydantic import BaseModel

class CatModel(BaseModel):
    id: int
    name: str
    owner: str