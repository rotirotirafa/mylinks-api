from pydantic import BaseModel

class LinksBodyRequestSchema(BaseModel):
    name: str
    url: str

class LinksQueryRequestSchema(BaseModel):
    link_id: int