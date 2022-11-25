import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="suresh123"
)

my_cursor = mydb.cursor()

sql_createDB_cmd = "CREATE DATABASE sureshdb;"
my_cursor.execute(sql_createDB_cmd)

sql_cmd = "DROP DATABASE sureshdb"

sql_showDBs_cmd = "SHOW DATABASES;"
my_cursor.execute(sql_showDBs_cmd)

for db in my_cursor:
    print('\t{}'.format(db))

sql_cmd = "CONNECT sureshdb;"
my_cursor.execute(sql_cmd)
