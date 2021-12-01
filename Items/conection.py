import psycopg2

connection = psycopg2.connect(host='plop.inf.udec.cl',database="bdi2021ah", user="bdi2021ah",
                              password="bdi2021ah")

cursor = connection.cursor()
cursor.execute("<Codigo en sql>")
print(cursor.fetchall())
connection.close()
