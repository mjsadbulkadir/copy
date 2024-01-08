import mysql.connector as msc
# a= msc.connect(host='localhost',user="root",password="root",database='database1')
# print(a)
  
  
class Connector:
    def __init__(self):
      self.a= msc.connect(host='localhost',user="root",password="root",database='database1')  
      query = "create table if not exists example1(user_id int primary key,name varchar(20),roll int, phone_no bigint )"
      b =self.a.cursor()
      b.execute(query)
      
    def insert_data(self,id,name,roll,phone):
      query = "insert into example1(user_id,name,roll,phone_no)values({},'{}',{},{})".format(id,name,roll,phone)
      b=self.a.cursor()
      b.execute(query)
      self.a.commit()  
      
    def read_data(self):
      query = "select * from example1"
      b=self.a.cursor()
      b.execute(query)
      
    def update_data(self,user_id, new_name, new_roll, new_phone_no):
      query="update exaple set name='{}',roll={},phone_no={} where user_id={}".format(new_name,new_roll,new_phone_no,user_id)
      b=self.a.cursor()
      b.execute(query)
      b.commit()
      print("data updated")
  
    def delete_data(self,user_id):
      query="delete from example1 where user_id={}".format(user_id)
      b=self.a.cursor()
      self.a.execute(query)
      self.a.commit()
      print("data delete")

obj1=Connector()
# obj1.insert_data(1,'abdul',10,1234567890)
obj1.insert_data(2,'faiz',11,1234567890)

          