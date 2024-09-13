from services.cliente_services import cadastro_cliente, listar_clientes
from services.pizza_services import cadastro_pizza, listar_pizzas

op = int(input('Digite a opção: [1- pizza, 2 - cliente, 3- venda]: '))

def main():
    if op == 1:
       cadastro_pizza()
    elif op == 2:
       cadastro_cliente()
    elif op == 3:
       listar_pizzas()
       print('')
       listar_clientes()

if __name__ == '__main__':
    main()
    

    