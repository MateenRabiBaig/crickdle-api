from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    country: str
    role: str
    batting_style: str
    bowling_style: str
    ipl_team: Optional[str] = None