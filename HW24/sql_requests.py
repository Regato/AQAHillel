from psycopg2 import connect


# Connecting to the database "store"
connection = connect(host='localhost', user='postgres',
                     password='HelloWorld12345',
                     dbname='store', port=5432
                     )

# Taking a cursor from the connection
db_cursor = connection.cursor()

# SQL query to execute
sql_query = '''INSERT INTO products("name", "price") VALUES ('tomato', 150),
                                                            ('orange', 200), 
                                                            ('potato', 160), 
                                                            ('apple', 80);
                                                            UPDATE products
                                                            SET price = 1000000
                                                            FROM orders
                                                            WHERE quantity < 10;
                                                            DELETE FROM orders
                                                            WHERE ORDERS.quantity > 10;'''


# Executing SQL query
db_cursor.execute(sql_query)
# Committing changes
connection.commit()
# Closing connection
connection.close()
