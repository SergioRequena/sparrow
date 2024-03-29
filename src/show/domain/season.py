from typing import List

from pydantic import BaseModel


class Season(BaseModel):
    number: int
    episode_count: int
    episodes: List = []
