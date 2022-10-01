from psycopg import connect

connection = connect(host='localhost', user='postgres',
                     password='HelloWorld12345',
                     dbname='store', port=5432
                     )

db_cursor = connection.cursor()

db_cursor.executemany("INSERT INTO products(\"name", "price\") VALUES "
                                                     "('tomato', 150), "
                                                     "('orange', 200), "
                                                     "('potato', 160), "
                                                     "('apple', 80);"
                                                     "UPDATE products "
                                                     "SET price = 1000000 "
                                                     "FROM orders "
                                                     "WHERE quantity < 10;"
                                                     "DELETE FROM orders "
                                                     "WHERE ORDERS.quantity > 10;"
                      )
