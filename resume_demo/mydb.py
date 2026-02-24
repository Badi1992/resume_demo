import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="technicalcoursesql", host="localhost", port=5433)

cursor = connection.cursor()

cursor.execute("SELECT * from portal.portal_users;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)