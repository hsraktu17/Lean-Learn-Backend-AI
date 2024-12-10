from pydantic import BaseModel
from typing import List

class FillQuestionSchema(BaseModel):
    id: str
    topic: str
    question: str
    choices: List[str]
    answers: List[str]
    resource: List[str]
    used: bool