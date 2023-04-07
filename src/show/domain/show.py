from pydantic import BaseModel
from typing import List

from src.show.domain.season import Season


class Show(BaseModel):
    id: int
    name: str
    seasons: List[Season]
