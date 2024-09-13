from database.connection import conn
from typing import Optional

class Cliente:
    def __init__(self, idcliente: Optional[int] = None, nome: str = '', 
                 cpf: str = '', 
                 telefone: str = '',
                 endereco: str = '',
                 email: str = ''):
        self.idcliente = idcliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def cadastrar(self):
        connection = conn()
        try:
            with connection:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO cliente (nome, cpf, telefone, endereco, email ) VALUES (%s, %s, %s, %s, %s)'
                    dados = (self.nome, self.cpf, self.telefone, self.endereco, self.email)
                    cursor.execute(sql, dados)
                    self.idcliente = cursor.lastrowid
                connection.commit()
        except Exception as e:
            print(f"Erro ao cadastrar o cliente: {e}")
