from pydantic import BaseModel


class Season(BaseModel):
    number: int
    episodes: int
