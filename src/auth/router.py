from fastapi import APIRouter, HTTPException, Response, Depends
from authx import AuthX, AuthXConfig, RequestToken

from .chems import UserLoginShema

router = APIRouter(prefix="/auth",
                   tags=["Авторизация 🔩"])

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

#Аутентификация 
@router.post("/login", summary = "Регистрация пользователей")
def login(creds: UserLoginShema, response: Response):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid = "12") #создание токена доступа, с хранением id 
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token) #добавляем в куки токен доступа в браузере
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Неправильный юзернэйм или пароль")

#Авторизация
@router.get("/protected", dependencies = [Depends(security.access_token_required)], summary = "Проверка на зарегестрированность") #класс Depends устанавливает зависимоть, то есть если у пользователя нет токена доступа, енд поинт не заработает
def protected():
    return {"comment": "Вы авторизованы"}