from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router


app = FastAPI()

origins = [
    # '*',
    "https://node2301.ebesesk.synology.me",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.0.43:7080/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)

# @app.get("/hello")
# async def hello():
#     return {"message": "안녕하세요 파이보"}


# uvicorn main:app --reload --host 0.0.0.0 --port 7443