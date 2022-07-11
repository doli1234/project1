from ast import Delete
from dataclasses import fields
import email
from email.mime import image
from itertools import product
from msilib import Table
from msilib.schema import tables
from re import S
from tarfile import RECORDSIZE


from unicodedata import name
from uuid import RFC_4122

from db import cursor,conn
from function import delete, excution_query, insert,select, update


#               varibles wich paas when function call       
def user_insert(name,password,email):
#                            column name in databse
    sql="INSERT INTO users (user_name,user_email,user_pass) VALUES ('%s', '%s', '%s')"
#                       varible wich get from calling funtion and passing for place of %s
    cursor.execute(sql%(name,password,email))
    conn.commit()
    print("data insert")

def user_fetchdata(id): 
    #sql="select * from users where user_id = %s" 
    sql="select p.*,c.comp_name from product p left join company c on p.company_id = c.id where pro_id = %s"
    cursor.execute(sql%(id))
    data = cursor.fetchone()
    return data

def user_fetchall(): 
    sql="select * from users" 
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def user_del(id):
    sql="delete from users where user_id = %s"
    cursor.execute(sql%id)
    conn.commit()
    print("data delete")

def user_update(name,email,password,id):
    sql="update users set user_name= '%s' , user_email= '%s' , user_pass= '%s' where user_id= %s"
    cursor.execute(sql%(name,email,password,id))
    conn.commit()
    print("updated")

def login_data(email,passowrd):
    sql="select * from users where user_email= '%s' AND user_pass= '%s'"
    cursor.execute(sql%(email,passowrd))
    data = cursor.fetchone()
    return data

# for product

def product_insert(name,image,price,desc,size):
    
    #sql="insert into product (pro_name ,pro_image ,pro_price ,pro_desc ,pro_size) values ('%s' ,'%s' ,'%s','%s','%s')"
    #cursor.execute(sql%(name,image,price,desc,size))
    #conn.commit()
    
    fields = """ "pro_name","pro_image","pro_price","pro_desc","pro_size" """
    data = [name,image,price,desc,size]
    record = insert('product',fields,data)
    return record

# excution_query("sql",)
# print("data insert")

#fetch one product
def fetch_product(id):
    #sql="select * from product where pro_id = %s"
    #cursor.execute(sql%id)
    #data = cursor.fetchone()
    # #return dict(data)
    fields = "*"
    where = "where pro_id = %s"%id
    record = select('product',fields,where)
    return record

#fetch all product
def fetch_all():
    #sql="select * from product "
    #cursor.execute(sql)
   # data = cursor.fetchall()
    fields =  " * "
    where = " "  
    record= select('product',fields,where,many=True)
    print(record)
    return record
    '''l1 = []
    for i in data:
        r1 = dict(i)
        l1.append(r1)
    return l1'''
    
#delete product
def del_pro(id):
    #sql= "delete from product where pro_id = %s"
    #cursor.execute(sql%id)
    #conn.commit()
    #excution_query(sql%id)
    #print("data deleted")
    fields = "*"
    where = "where = %s"%id
    record = delete('product',fields,where)
    return record

#update product
def update_pro(name,image,price,desc,size,id):
    #sql="update product set pro_name= '%s' ,pro_image='%s' ,pro_price='%s', pro_desc= '%s',pro_size='%s' where pro_id = %s"
    #cursor.execute(sql%(name,image,price,desc,size,id))
    #conn.commit()
    #print("data updated")
    fields = """ pro_name = %s,pro_image = %s,pro_price = %s,pro_desc = %s,pro_size = %s """
    where = "where pro_id = %s"%id
    data = [name,image,price,desc,size]
    record = update('product',fields,data,where)
    return record

def company_data(comp_name):
    #sql="INSERT INTO company(comp_name)VALUES('%s')"
    #cursor.execute(sql%(comp_name))
    #conn.commit()
    #print("company data add")
    fields = """ "comp_name" """
    data = [comp_name]
    record =insert('company',fields,data)
    return record


