import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='176.53.62.121',
                             port='8889',
                             user='simm_pyuser',
                             password='B07fEJsL+gs-',
                             db='simm_pydeneme',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `denemetable`"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
