
import email
from email.mime import image
import json
import os
from tkinter import image_names
from unicodedata import name
from xml.dom.minidom import Identified
from crud import *
from psycopg2 import*

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
user_image_path='media//user'
app = Flask(__name__)
#insert data or sign up
@app.route("/user_add",methods=['POST'])
def user_add():
#  (variabele)       (from postman)
    name = request.json['name']
    password = request.json['pass']
    email = request.json['email']
#               varible wich created above                
    user_insert(name,password,email)
    return jsonify("data inserted successfully")

# fetch one data 
@app.route("/user_fetch/<int:id>",methods=['POST'])
def user_fetch(id):
    data = user_fetchdata(id)
    return jsonify(data)

#fetch all data
@app.route("/user_alldata",methods=['POST'])
def user_alldata():
    data = user_fetchall()
    return jsonify(data)

#delete data
@app.route("/user_deldata/<int:id>",methods=['POST'])
def user_deldata(id):
    data = user_del(id)
    return jsonify(data)

#update data
@app.route("/user_updata/<int:id>",methods=['POST'])
def user_updata(id):
    name= request.json['name']
    email=request.json['email']
    password=request.json['pass']

    user_update(name,email,password,id)
    return jsonify("data updated sucessfully")

@app.route("/login",methods=['POST'])
def login():
    email=request.json['email']
    password= request.json['pass']

    data = login_data(email,password)
    if data == None:
        return jsonify ("wrong password")
    else:
        return jsonify (data)
#-------------------------------------------------------------------------------------------------------------------------------------------
#for product insert

@app.route("/product_add",methods=['POST'])
def product_add():
    name= str(request.form['name'])
    image= str(request.files['img'])
    price= str(request.form['price'])
    desc= str(request.form['desc'])
    size= str(request.form['size'])
    image=secure_filename(request.files['img'].filename)

    product_insert(name,image,price,desc,size)
    return jsonify("data inserted succesfully")

# fetch one product
@app.route("/product_fetch/<int:id>",methods=['POST'])
def product_fetch(id):
    data = fetch_product(id)
    print(data)
    image_names = data['pro_image']
    #to create link
    str_image=os.path.join(os.path.abspath(os.path.dirname(__file__)),user_image_path,image_names)
    data['pro_image'] = str_image

    return jsonify(data)
   

#fetch all product
@app.route("/product_all",methods=['POST'])
def product_all():
    data = fetch_all()
    return jsonify(data)

#delete product
@app.route("/product_del/<int:id>",methods=['POST'])
def product_del(id):
    data = del_pro(id)
    return jsonify (data)

#update product
@app.route("/product_update/<int:id>",methods=['POST'])
def product_update(id):
    name= str(request.form['name'])
    image= request.files['img']
    price= str(request.form['price'])
    desc= str(request.form['desc'])
    size= str(request.form['size'])
    print(image)
    #create file name
    product_img_name= secure_filename(image.filename)
    #create image link
    image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),user_image_path,product_img_name))

    update_pro(name,product_img_name,price,desc,size,id)
    return jsonify ("data updated sucessfully")  

@app.route("/company",methods=['POST'])
def company():
    name = request.json['name']
    company_data(name)
    return jsonify ("your record sucessfully inserted")

    













if __name__== "__main__":
    app.run(debug=True)