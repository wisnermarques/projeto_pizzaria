from database.connection import conn

def venda(idpizza, idcategoria, idcliente=None):  
    try: 
        with conn() as connection:
            with connection.cursor() as cursor:
                if idcliente:
                    sql = 'INSERT INTO venda (idpizza, idcategoria, idcliente) VALUES (%s, %s, %s)'
                    dados = (idpizza, idcategoria, idcliente)
                else:
                    sql = 'INSERT INTO venda (idpizza, idcategoria) VALUES (%s, %s)'
                    dados = (idpizza, idcategoria)

                cursor.execute(sql, dados)
                
                # Capturando e exibindo o último ID inserido
                print(f"Cadastro realizado com sucesso. ID da venda: {cursor.lastrowid}")
            connection.commit()
    except Exception as e:
        print(f'Erro ao realizar o pedido: {e}')
       
