from database.connection import conn

def venda(idpizza, idcategoria, idcliente):
        connection = conn()
        try:
            with connection:
                if idcliente:
                    with connection.cursor() as cursor:
                        sql = 'INSERT INTO venda (idpizza, idcategoria, idcliente) VALUES (%s, %s, %s)'
                        dados = (idpizza, idcategoria, idcliente)
                        cursor.execute(sql, dados)
                    connection.commit()
                else:
                    with connection.cursor() as cursor:
                        sql = 'INSERT INTO venda (idpizza, idcategoria) VALUES (%s, %s)'
                        dados = (idpizza, idcategoria, idcliente)
                        cursor.execute(sql, dados)
                    connection.commit()
        except Exception as e:
            print(f"Erro ao cadastrar a pizza: {e}")
    
    