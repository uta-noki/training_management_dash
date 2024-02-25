import mysql.connector

# MySQLデータベースに接続
class Utileties_DB:
    
    def __init__(self,host_num="0.0.0.0",port_num=8050,user_name="shinozaki",password_name="yuta",database_name="training_record"):
        
        self.host_num = host_num
        self.port_num = port_num
        self.user_name = user_name
        self.password_name = password_name
        self.database_name = database_name
        self.mydb = mysql.connector.connect(
            host=self.host_num,
            port=self.port_num,
            user=self.user_name,
            password=self.password_name,
            database=self.database_name
        )
        
    def out(self):
        print(self.host_num)