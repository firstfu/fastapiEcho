from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {
        "code": 200,
        "statusCode": 2001,
        "message": "測試api",
        "data": {
            "name": "test",
            "age": 18,
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
