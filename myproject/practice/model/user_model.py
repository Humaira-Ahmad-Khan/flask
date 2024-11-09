import mysql.connector
class Tea():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost' , user='root' , password='qwerty.' , database='flask_learing' )
            self.cur = self.con.cursor(dictionary=True)
                       
            print('connection is connected')
        except:
            print('connection is failed')           
        
    
    def humaira(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        
        return result
    
    
     