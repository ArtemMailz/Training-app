from fastapi import APIRouter, HTTPException
from database import async_session
from .model import DogModel
from .chemas import DogShemas

from sqlalchemy import select, insert, delete, update, and_

router = APIRouter(prefix = "/db_function",
                   tags = ["Собачки 🐺"])
    

@router.get("/all_dog", summary = "Получение всех собачек из бд")
async def get_all_dog() -> list[DogShemas]:
    try:
        async with async_session() as session:
            query = (
                select(DogModel)
            )

            result = await session.execute(query)
            return result.scalars().all()
    
    except Exception:
        raise HTTPException(status_code = 404, detail = {
            "status": 404,
            "detail": None,
            "comment": "Собаки не были найдены"
        })
    
@router.post("/add_dog", summary = "Добавление собачки в бд")
async def add_dogs(new_dog: DogShemas):
    try:
        async with async_session() as session:
            query = (
                insert(DogModel)
                .values(name = new_dog.name,
                        age = new_dog.age)
            )

            await session.execute(query)
            await session.commit()
            return {"status": 200,
                    "detail": None,
                    "comment": "Новая собака добавлена"}
        
    except Exception:
        raise HTTPException(status_code = 500, detail = {"status": 500,
                "detail": None,
                "comment": "Ошибка сервера, операция не выполнена"})

@router.delete("/delete_dog/{dog_id}", summary = "Удаление собачки по id из бд")
async def delete_dog(dog_id: int):
    try:
        async with async_session() as session:
            query = (
                delete(DogModel)
                .where(DogModel.id == dog_id)
            )

            await session.execute(query)
            await session.commit()
            return {"status": 200,
                    "detail": None,
                    "comment": f"Собака номер {dog_id} успешно удалена"}
        
    except Exception:
        raise HTTPException(status_code = 500, detail = {"status": 500,
                "detail": None,
                "comment": "Ошибка сервера, операция не выполнена"})
    
@router.patch("/update_dog", summary = "Изменение имени собачки по id в бд")
async def update_dog(dog_id: int, dog_name: str):
    try:
        async with async_session() as session:
            query = (
                update(DogModel)
                .where(DogModel.id == dog_id)
                .values(name = dog_name)
            )

            await session.execute(query)
            await session.commit()
            return {"status": 200,
                    "detail": None,
                    "comment": f"Имя собаки номер {dog_id} успешно измененно на {dog_name}"}
        
    except Exception:
        raise HTTPException(status_code = 500, detail = {"status": 500,
                "detail": None,
                "comment": "Ошибка сервера, операция не выполнена"})
    

@router.get("/dog", summary = "Получение собачек по возрату из бд")
async def get_dog(min_age: int, max_age: int):
    async with async_session() as session:
        query = (
            select(DogModel.name)
            .where(and_(DogModel.age >= min_age,
                        DogModel.age <= max_age))
        )
        
        result = await session.execute(query)
        return result.scalars().all() 