from services.cliente_services import cadastro_cliente, obter_idcliente
from services.pizza_services import cadastro_pizza, listar_pizzas
from services.venda import venda

def main():
    op = int(input('Digite a opção: [1- pizza, 2 - cliente, 3- venda]: '))
    if op == 1:
       cadastro_pizza()
    elif op == 2:
       cadastro_cliente()
    elif op == 3:
      listar_pizzas()
      print('')
      idpizza = int(input('Informe o id da pizza: '))
      idcategoria = int(input('Informe o id da categoria: '))
      cliente = input('Deseja informa o cliente [S-Sim, N-Não]? ')
      if cliente.upper() == 'S':
         cpf = input('Informe o cpf do cliente: ')
         cliente = obter_idcliente(cpf)
         venda(idpizza=idpizza, idcategoria=idcategoria, idcliente=cliente['idcliente'])
      else:
         venda(idpizza=idpizza, idcategoria=idcategoria, idcliente=None)
         
if __name__ == '__main__':
    main()
    

    