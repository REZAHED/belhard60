from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class Category(BaseModel):
    name : str = Field(title='NAME')
    id: int = Field(title="unique identity")

@app.get('/')
async def index():

    return "hello"

@app.get('/category',response_model=Category)
async def get_category(category_id:int = Query(ge = 1)):
    category =Category(id=category_id, name=f'category{category_id}')
    return category