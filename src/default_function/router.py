from fastapi import APIRouter, HTTPException

from .chems import CatModel

router = APIRouter(prefix = "/dafault",
                    tags = ["Котики 🐱"])

cats = [
    {
        "id": 1,
        "name": "Tima",
        "owner": "Kira",
        "old": 14,
        "email": "user@example.com"
    },
    {
        "id": 2,
        "name": "Klepa",
        "owner": "Mather Kira",
        "old": 1,
        "email": "user@example.com"
    }
]


@router.get("/cats", summary = "Получение всех котиков")
def read_cats() -> list[CatModel]:
    return cats


@router.get("/cats/{cats_id}", summary = "Получение конкретного котика")
def read_cats(cats_id: int):
    for cat in cats: 
        if cat["id"] == cats_id:
            return cat
    raise HTTPException(status_code = 404, detail = "Книга не найдена")


@router.post("/add_cat", summary = "Добавление котика")
def add_cat(cat: CatModel):
        cats.dafault_routerend(cat)
        return {"status": 200, "detail": "Кот успешно добавлен"}