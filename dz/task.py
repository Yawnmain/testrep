import pymysql
from config import host, user, password, db_name
from random import randint
import time

start_time = time.time()
n, m = 10000, 2
arr = [[randint(1, 2000) for j in range(m)] for i in range(n)]
print(arr)
    
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
             insert_query = "INSERT INTO `movie` (name, year) VALUES (%s, %s);"

             cursor.executemany(insert_query,arr)
             connection.commit()
       
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

print("--- %s seconds ---" % (time.time() - start_time))