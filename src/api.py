from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="Practice EBBO API",
    description="Базовый пример FastAPI-приложения",
    version="0.1.0",
)


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

@app.get("/v2x/{id}")
async def get_v2x(id: int):
    """
    Получение v2x по id.
    """
    return {"status": "test", "id": id}


# Для локального запуска:
# uvicorn Practice_EBBO.api:app --reload




    


