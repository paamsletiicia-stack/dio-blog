import sqlalchemy as sa
from database import metadata

# unique=True    -> quer dizer que nunca 2 titulos podem ser iguais
# nullable=True  -> pode ser nulo, ex "published_at=null"
# nullable=False -> não e permitido passar valor null, obrigatorio ter um valor 
# default=False  -> Valor padrão como False, caso não informe o valor do campo.
posts = sa.Table(
    "posts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(150), nullable=False, unique=True),
    sa.Column("content", sa.String, nullable=False),
    sa.Column("published_at", sa.DateTime, nullable=True),
    sa.Column("published", sa.Boolean, default=False),
)
