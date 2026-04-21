from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# import jwt
# from jwt import InvalidTokenError
from pydantic import Json
import requests

app = FastAPI(
    title="Practice EBBO API",
    description="Базовый пример FastAPI-приложения",
    version="0.1.0",
)

# Секретный ключ для подписи JWT
# В реальном проекте храни это в .env
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

# Схема Bearer Token
security = HTTPBearer()


# def verify_jwt_token(
#     credentials: HTTPAuthorizationCredentials = Depends(security),
# ):
#     token = credentials.credentials

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except InvalidTokenError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Невалидный или просроченный токен",
#         )


@app.get("/")
async def root():
    """
    Базовый эндпоинт для проверки, что сервер работает.
    """
    return {"message": "Hello from FastAPI!"}


@app.get("/ping")
async def ping():
    """
    Простой health-check эндпоинт.
    """
    return {"status": "ok"}


# @app.get("/v2x/{id}")
# async def get_v2x(id: int, payload: dict = Depends(verify_jwt_token)):
#     """
#     Получение v2x по id только при наличии валидного JWT.
#     """
#     return {
#         "status": "test",
#         "id": id,
#         "user": payload,
#     }


@app.get("/local/event")
async def send_event():
    """
    Отправка события в локальную систему.
    """
    response = requests.get("http://127.0.0.1:8000/eventProcessor/event-receiver")
    return {"status": "event is ok", "response": response.json()}

# Для локального запуска:
# uvicorn Practice_EBBO.api:app --reload

if __name__ == "__main__":
    import uvicorn
    # Запускаем именно на 8000 порту, как указано в условии
    uvicorn.run(app, host="0.0.0.0", port=8080)