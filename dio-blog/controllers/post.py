from typing import Annotated
from datetime import UTC, datetime

from fastapi import Cookie, Header, Response, status, APIRouter

from schemas.post import PostIn
from views.post import PostOut

from main import app

router = APIRouter()


# class Post(BaseModel):
#     title: str
#     date: datetime = datetime.now(UTC)
#     published: bool = False



fake_db = [

    {"title": "Criando uma aplicação com Djanco",
        "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com FastAPI",
        "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Flask",
        "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Starlett",
        "date": datetime.now(UTC), 'published': False},

]

@router.post('/posts/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    # .model_dump() vai retornar a representação desta classe em um dicionario
    return post



@router.post('/posts/', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    # .model_dump() vai retornar a representação desta classe em um dicionario
    return post

@router.get("/posts/", response_model=list[PostOut])
def read_post(response:Response ,published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None,
              user_agent: Annotated[str | None, Header()] = None ,):
    response.set_cookie(key="user", value="Pam@hotmail.com")
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")

    lista_retorno = []
    for fake in fake_db:
        if len(lista_retorno) == limit:
            break
        if fake["published"] is published:
            lista_retorno.append(fake)

    return lista_retorno

@router.get("/posts/{framework}", response_model=PostOut)  # <-- isso e chamado de verbo ou rota
# a palavra 'posts' é o nome da ROTA e {framework} é uma variavel de entrada onde alguem vai informar
def read_framework_posts(framework: str):
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
