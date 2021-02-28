import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost', 
  port=3306, 
  user='root', 
  passwd='adminx', 
  db='Peterest', 
  charset='utf8mb4', 
  cursorclass=pymysql.cursors.DictCursor)


print("\nDatabase Connection works!\n")