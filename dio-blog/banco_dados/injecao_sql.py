import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente:")
cursor.execute("SELECT * FROM clientes Where id=?", (id_cliente,))
cliente = cursor.fetchall()

for cliente in cliente:
    print(dict(cliente))

    #id_cliente = input("Informe o id do cliente:")
    #cursor.execute(f"SELECT * FROM clientes Where id={id_cliente}")  FORMA INCORRETA