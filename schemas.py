from pydantic import BaseModel


class LinksSchema(BaseModel):
    id: int
    full_link: str
    short_link: str

    class Config:
        orm_mode = True
