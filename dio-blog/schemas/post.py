from fastapi import FastAPI
from datetime import UTC, datetime
from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    content: str
    date: datetime = datetime.now(UTC)
    published: bool = False
