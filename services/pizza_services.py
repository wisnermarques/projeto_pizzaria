from database.connection import conn
from models.pizza import Pizza

def cadastro_pizza():
        try:
            p = Pizza(sabor='Calabresa ao alho', descricao='Mussarela, molho, tomate, calabresa, cebola e orégano')
            p.cadastrar()
            if p.idpizza:
                print('Cadastro realizado com sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

def listar_pizzas():
        connection = conn()
        try:
            with connection:
                with connection.cursor() as cursor:
                    sql = 'SELECT * FROM pizza;'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for pizza in result:
                        print(pizza)
        except Exception as e:
            print(f"Erro ao listar as pizzas: {e}")

     