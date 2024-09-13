from services.cadastro_cliente import cadastro_cliente
from services.cadastro_pizza import cadastro_pizza

op = int(input('Digite a opção: [1- pizza, 2 - cliente]: '))

def main():
    if op == 1:
       cadastro_pizza()
    elif op == 2:
       cadastro_cliente()

if __name__ == '__main__':
    main()

    