import pymysql 
 
from secrets import endpoint, DB_user, DB_pass, DB_name, DB_query 

connection = pymysql.connect(host = endpoint, user = DB_user, password = DB_pass, db = DB_name)

def handler(event, context):
    cursor = connection.cursor()
    cursor.execute(DB_query)

    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))



