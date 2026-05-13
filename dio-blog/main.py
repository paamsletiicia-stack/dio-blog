from fastapi import FastAPI
from datetime import UTC, datetime

app = FastAPI()


@app.get("/posts/{framework}")  # <-- isso e chamado de verbo ou rota
def read_posts(framework: str):
    return {
        "posts": [
            {
                "title": f"Criando aplicação com {framework}",
                "date": datetime.now(UTC),
            },
            {
                "title": f"Internacionalizando uma APP {framework}",
                "date": datetime.now(UTC),
            },
        ]
    }
