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