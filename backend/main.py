from fastapi import FastAPI

app = FastAPI(
    title="Universal Robot Brain",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "project": "Universal Robot Brain",
        "status": "online"
    }