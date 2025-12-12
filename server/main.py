from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Hello World"}

if __name__ == "__main__":
    # The uvicorn.run command starts the server
    # --port 5000 sets the server to run on port 5000 (as requested)
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)