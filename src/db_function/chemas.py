from pydantic import BaseModel
 
class DogShemas(BaseModel):
    id: int 
    name: str
    age: int