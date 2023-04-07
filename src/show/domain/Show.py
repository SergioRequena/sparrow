from pydantic import BaseModel
from typing import List
from src.show.domain import Season


class Show(BaseModel):
    id: int
    name: str
    seasons: List[Season]
