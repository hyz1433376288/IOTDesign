import pymysql

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

