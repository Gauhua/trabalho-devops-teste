from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def teste1():
    return {"teste": True, "num_aleatorio": random.randint(1, 10000)}