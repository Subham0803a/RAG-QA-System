from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Hello World"}

@app.get("/root")
def testing():
    return {"message": "This is root endpoint"}

if __name__ == "__main__":
    # The uvicorn.run command starts the server
    # --port 5000 sets the server to run on port 5000
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)