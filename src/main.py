from fastapi import FastAPI
import uvicorn

from default_function.router import router as dafault_router

app = FastAPI(title = "Training App")

app.include_router(dafault_router)
 
if __name__ == "__main__":
    uvicorn.run(app = "main:app", reload = True)