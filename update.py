# Update banco de dados
import pymysql

def update_sql():
    try:
        # Conexão com o banco de dados para fazer o update  
        host = "xx.xx.xx.xx"  
        user = "user_db"       
        password = "password_db"           
        database = "nome_db"
        conn  = pymysql.connect(host=host, user=user, password=password, database=database) 
        cursor = conn.cursor()
        
        update_status = f'UPDATE tb_carrinho set leitura_robo = 1, status_Final = {id_status_cotacao} where id_carrinho = {id_carrinho};'
        cursor.execute(update_status)
        
        data = cursor.fetchall()
        conn.commit()
        conn.close()
        print('Update realizado Id Carrinho', id_carrinho)

    except:
        print('Não possivel dar o update no banco')

update_sql()