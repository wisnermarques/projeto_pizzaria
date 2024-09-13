from database.connection import conn
from typing import Optional

class Pizza:
    def __init__(self, idpizza: Optional[int] = None, sabor: str = '', descricao: str = ''):
        self.idpizza = idpizza
        self.sabor = sabor
        self.descricao = descricao

    def cadastrar(self):
        connection = conn()
        try:
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO pizza (sabor, descricao) VALUES (%s, %s)'
                    dados = (self.sabor, self.descricao)
                    cursor.execute(sql, dados)
                    self.idpizza = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Erro ao cadastrar a pizza: {e}")
    
    