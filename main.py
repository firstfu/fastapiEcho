from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "fastapi Hello World",
        "status": 200,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)