from fastapi import FastAPI

app = FastAPI()


# route creation using decoratoe @ using get method
@app.get("/")
def hello():
    return {'messages':'hello World'}

# to run th code -> uvicorn main:app --reload -> here main is file name

# another route
@app.get('/about')
def about():
    return {'messages':'This is the first FASTAPI app'}




