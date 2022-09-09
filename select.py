#Select banco de dados Python
import pymysql

def select_sql():
    try:
        # Conexão com o banco de dados para pegar o status
        host = "xx.xx.xx.xx"  
        user = "user_db"       
        password = "password_db"           
        database = "nome_db"
        conn  = pymysql.connect(host=host, user=user, password=password, database=database) 
        cursor = conn.cursor()

        busca_status = f'''SELECT 
        num_status from dbteste.tb_status_ where descricao_status = "{analise_idx}" 
        '''

        cursor.execute(busca_status)

        
        data = cursor.fetchall()
        conn.close()

        for buscaBanco in data:
            id_status_cotacao = buscaBanco[0]
        print('Id da viabilidade: ',id_status_cotacao)
    
    except:
        print('Não foi possivel pegar o id do status')

select_sql()