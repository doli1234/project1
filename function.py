from math import perm
from posixpath import split

from tkinter import INSERT




#from psycopg2 import cursor
from db import cursor,conn
from psycopg2 import *

def excution_query(sql,peram,many=False):
    query  = sql.split()
    if query[0]== "INSERT":
        if many:
            print(peram)
            cursor.executemany(sql,peram)
            conn.commit()
        else:
            print(sql)
            cursor.execute(sql,peram)
            conn.commit()
            return cursor.fetchone()
    if query[0]== "UPDATE":
        cursor.execute(sql,peram)
        conn.commit()
        return cursor.fetchone() 
    if query[0]== "DELETE":
        cursor.execute(sql,peram)
        conn.commit() 
    if query[0]=="SELECT":
        if many:
            print(peram)
            cursor.execute(sql)
            return cursor.fetchall()   
        else:
            cursor.execute(sql)
            return cursor. fetchone()
     
def insert(table ,fields,data,many=False):
    print(type(table))
    print(fields)
    print(type(data))
    sql= " INSERT into " +table+ "(" + fields + " ) values("
    print(fields)
    print(data)
    if many:
        temp_data = data[0]
    else:
        temp_data = data
    for i in temp_data:
        sql = sql+"%s,"
    sql = sql.rstrip(sql[-1])
    sql = sql + ") RETURNING *"
    record = excution_query(sql,data,many)
    return record

def update(table,fields,data,where):
    sql = "UPDATE " +table+ " set " +fields+where+" RETURNING *"
    print(sql)
    record = excution_query(sql,data,many=True)
    return record

def delete(table,where=""):
    sql = "delete from" +table + where
    excution_query(sql,())

def select(table,fields,where="",many=False):
    sql = "SELECT " +fields+ " FROM " +table
    #excution_query(sql,(),many)
    sql = sql +" "+ where
    print(sql)
    record = excution_query(sql,(),many)
    return record  


    