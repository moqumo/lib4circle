import os
import uvicorn  # pyright: ignore
from dotenv import load_dotenv  # pyright: ignore
from fastapi import FastAPI  # pyright: ignore
from fastapi.middleware.cors import CORSMiddleware  # pyright: ignore

app = FastAPI()
load_dotenv(verbose=True)

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(os.environ.get("FRONTEND_ORIGIN"))],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/isbn/{isbn}")
async def read_item(isbn: str):
    print("isbn:", isbn)
    message = "no problem"
    if len(isbn) != 13:
        message = "ISBN must be 13 digits"
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app)
