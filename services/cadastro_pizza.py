from models.pizza import Pizza


def cadastro_pizza():
        try:
            p = Pizza(sabor='Calabresa ao alho', descricao='Mussarela, molho, tomate, calabresa, cebola e orégano')
            p.cadastrar()
            if p.idpizza:
                print('Cadastro realizado com sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')