import pymysql
from werkzeug.security import generate_password_hash
conn=pymysql.Connect(host='49.234.72.229',port=3306,database='iot',user='root',password='hyz@112488',charset='utf8')
cur=conn.cursor()

def insert(username,password):
  sql="insert into user (username,password) values ('%s','%s')"%(username,password)
  cur.execute(sql)
  conn.commit()
  conn.close()

def isExisted(username,password):

  sql="select * from iot_user where iot_username ='%s' and iot_password ='%s'"%(username,password)
  cur.execute(sql)
  result=cur.fetchall()
  if(len(result)==0):
    return False
  else:
    return True
def convert_hashpwd():
  sql="select iot_password from iot_user"
  cur.execute(sql)
  result=cur.fetchall()
  hashpwd=[]
  for i in range(0,len(result)):
    print(i)
    hashpwd.append(generate_password_hash(result[i][0]))
    sql="UPDATE iot_user  SET iot_password='hashpwd[i]' where iot_uid='%d'"%(i+1)
    cur.execute(sql)
    print(sql)
    print(hashpwd[i])
if __name__=="__main__":
  convert_hashpwd()