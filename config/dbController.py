import pymysql

con = pymysql.Connect(
  host='localhost', 
  user='root', 
  password='adminadmin', 
  db='Peterest', 
  charset='utf8', 
  cursorclass=pymysql.cursors.DictCursor, 
  port=3306)
