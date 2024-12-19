import uvicorn  # pyright: ignore
from fastapi import FastAPI  # pyright: ignore

app = FastAPI()


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
