from fastapi import FastAPI
from datetime import datetime


class PostIn(BaseModel):
    title: str
    content: str
