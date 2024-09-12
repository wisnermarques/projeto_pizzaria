import database.connection

class Pizza:
    def __init__(self, idpizza: None, sabor: str, descricao: str):
        self.idpizza = idpizza
        self.sabor = sabor
        self.descricao = descricao

    def cadastrar(self):
        connection = connection.conn()
        with connection:
            with connection.cursor() as cursor:
                sql = f'INSERT INTO pizza (sabor, descricao) VALUES (%s, %s)'
                dados = (self.sabor, self.descricao)
                cursor.execute(sql, dados)
                self.idpizza = cursor.lastrowid

p = Pizza('Calabresa ao alho', 'Mussarela, molho, tomate, calabresa, cebola e orégano')
p.cadastrar()