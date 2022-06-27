

import psycopg2
import psycopg2.extras

#establishing the connection
conn = psycopg2.connect(
    database = "project1" , user = 'postgres' , password = 'admin' , host = '127.0.0.1' , port = '5432'
)   

#create cursor object using tha cursor method ()
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#excute mysql function using the excute () method   
cursor.execute("select version()")

#fetch a single row using fetchone () method
data = cursor.fetchone()
print("establish connection: ", data)

#close the connection



