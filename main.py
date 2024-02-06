from flask import Flask, request, render_template
import pymysql 
import pymysql.cursors 

app = Flask(__name__)   
conn = pymysql.connect(
    host='10.100.33.60', 
    user = 'kwilliams4', 
    password='228426581', 
    database='kwilliams4_Astro',
    cursorclass=pymysql.cursors.DictCursor

) 

@app.route('/')
def index(): 
    return render_template('home.html.jinja')  


@app.route('/signup', methods =['GET','POST'])
def signup():  
    if request.method =="POST": 
        username = request.form['username'] 
        email = request.form['email'] 
        password = request.form['password']


        cursor = conn.cursor() 
        cursor.execute(f"INSERT INTO `Users` (Username, Email, Password) VALUES ('{username}', '{password}', '{email}')")
        cursor.close()
        conn.commit()
        


    return render_template('signup.html.jinja')  

@app.route('/signin', methods = ['GET', 'POST'])
def signin(): 
    if request.method =="POST": 
        username = request.form['username'] 
        email = request.form['email'] 
        password = request.form['password']


        cursor = conn.cursor() 
        cursor.execute(f"INSERT INTO `Users` (Username, Email, Password) VALUES ('{username}', '{password}', '{email}')")
        cursor.close()
        conn.commit()
        
