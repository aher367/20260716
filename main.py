from fastapi import FastAPI

app = FastAPI(
    title="Hello API",
    description="A simple API for Render deployment demonstration",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello"}
