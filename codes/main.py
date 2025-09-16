from fastapi import FastAPI
import json

app = FastAPI()

# load data from json file
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        
        return data
    
    
    
# route creation using decoratoe @ using get method
@app.get("/")
def hello():
    return {'messages':'Patient Management System API'}

# to run th code -> uvicorn main:app --reload -> here main is file name

# another route
@app.get('/about')
def about():
    return {'messages':'A fully functional API to manage your patient record'}

# new endpoint to give all the data to client
@app.get('/view')
def view():
    data = load_data()
    
    return data







