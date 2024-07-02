from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
async def get_data():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
