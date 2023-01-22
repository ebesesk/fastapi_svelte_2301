from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router


app = FastAPI()

origins = [
    '*',
    # "https://192.168.0.3"
    # "https://ya2301.ebesesk.synology.me/hello"
    # "http://192.168.0.3",
    # "http://127.0.0.1",
    # "http://127.0.0.1:5173",
    # "https://127.0.0.1:5173",
    # "http://localhost",
    # "http://localhost:5173",
    # "https://localhost:5173",
    # "http://192.168.0.43:7080",
    # "https://192.168.0.43:7080",
    # "http://node2301.ebesesk.synology.me/",
    # "https://node2301.ebesesk.synology.me",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)


# @app.get("/hello")
# async def hello():
#     return {"message": "안녕하세요 파이보"}


# uvicorn main:app --reload --host 0.0.0.0 --port 7443