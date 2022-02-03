from fastapi import FastAPI
from src.schemas.base_schema import LinksBodyRequestSchema

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "live"}

@app.get('/links')
def retrieve_links():
    return [
        {"name": "Facebook", "url": "http://facebook.com.br"}, 
        {"name": "Linkedin", "url": "http://linkedin.com/in/rotirotirafa"}
    ]

@app.post('/links')
def insert_link(body: LinksBodyRequestSchema):
    return body

@app.put('/links/{link_id}')
def insert_link(body: LinksBodyRequestSchema, link_id: int):
    return link_id

@app.delete('/links/{link_id}')
def insert_link(link_id: int):
    return link_id
