from fastapi import FastAPI
import uvicorn

from default_function.router import router as default_router
from db_function.router import router as db_route

app = FastAPI(title = "Training App")

@app.get("/")
def start_function():
    return {"status": 200}

app.include_router(default_router)
app.include_router(db_route)
 
if __name__ == "__main__":
    uvicorn.run(app = "main:app", reload = True)