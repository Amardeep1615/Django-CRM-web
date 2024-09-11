#pip install mysql-connector-python
import MySQLdb

try:
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Amar!@#123",
        database="rama"
    )
    print("Connection successful")
except MySQLdb.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Connection closed")



