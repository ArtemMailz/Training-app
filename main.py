from fastapi import FastAPI, HTTPException
import uvicorn

from model import CatModel

app = FastAPI(title = "Training App")


cats = [
    {
        "id": 1,
        "name": "Tima",
        "owner": "Kira"
    },
    {
        "id": 2,
        "name": "Klepa",
        "owner": "Mather Kira"
    }
]


@app.get("/cats", tags = ["Котики 🐱"], summary = "Получение всех котиков")
def read_cats():
    return cats

@app.get("/cats/{cats_id}", tags = ["Котики 🐱"], summary = "Получение конкретного котика")
def read_cats(cats_id: int):
    for cat in cats: 
        if cat["id"] == cats_id:
            return cat
    raise HTTPException(status_code = 404, detail = "Книга не найдена")

@app.post("/add_cat", tags = ["Котики 🐱"], summary = "Добавление котика")
def add_cat(cat: CatModel):
        cats.append(cat)
        return {"status": 200, "detail": "Кот успешно добавлен"}
 
if __name__ == "__main__":
    uvicorn.run(app = "main:app", reload = True)