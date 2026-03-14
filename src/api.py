from fastapi import FastAPI
from starlette.status import HTTP_200_OK

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

@app.get('/datchik/{type}/{is_active}')
async def get_datchik(type: str, is_active: bool):
    return {
        'status': HTTP_200_OK,
        'type': type,
        'is_active': is_active
    }

# Для локального запуска:
# uvicorn Practice_EBBO.api:app --reload


# deploy:
  #   needs: [test]
  #   runs-on: self-hosted

  #   steps:
  #     - uses: actions/checkout@v4

  #     - name: Deploy FastAPI
  #       run: |
  #         cd /home/server/project
  #         git pull
  #         source venv/bin/activate
  #         pip install -r requirements.txt
  #         sudo systemctl restart fastapi  

    


