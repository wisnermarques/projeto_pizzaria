from database.connection import conn
from models.cliente import Cliente

def cadastro_cliente():
        try:
            c = Cliente(nome='Pedro', cpf='32132132132', telefone='659762342', 
            endereco='Rua das Flores', email='p32@mail.com')
            c.cadastrar()
            if c.idcliente:
                print('Cadastro realizado com sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

def listar_clientes():
        connection = conn()
        try:
            with connection:
                with connection.cursor() as cursor:
                    sql = 'SELECT * FROM cliente;'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print(result)
        except Exception as e:
            print(f"Erro ao listar as pizzas: {e}")

def obter_idcliente(cpf: str):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT idcliente FROM cliente WHERE cpf = %s;'
                cursor.execute(sql, cpf)
                result = cursor.fetchone()
                return result
    except Exception as e:
            print(f"Erro ao localizar o cliente: {e}")