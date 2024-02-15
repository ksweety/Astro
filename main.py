from flask import Flask, request, render_template, url_for, redirect
import flask_login
import pymysql 
import pymysql.cursors 

app = Flask(__name__)  
app.secret_key = 'KKKmonkey21$'  
login_manager = flask_login.LoginManager()
login_manager.init_app(app)  

class User:
    is_authenticated = True 
    is_anonymous = False 
    is_active = True 

    def __init__(self, id, username):
        self.username = username
        self.id = id 
    def get_id(self): 
        return str(self.id)   

@login_manager.user_loader 
def load_user(user_id):
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM Users WHERE id = %s", (str(user_id),))

    result = cursor.fetchone() 
    cursor.close()
    conn.commit()

    if result is None: 
        return None   
    return User(result['ID'], result['Username'])

conn = pymysql.connect(
    host='10.100.33.60', 
    user = 'kwilliams4', 
    password='228426581', 
    database='kwilliams4_Astro',
    cursorclass=pymysql.cursors.DictCursor

) 

@app.route('/')
def index(): 
    if flask_login.current_user.is_authenticated:
        return redirect('/feed')
    return render_template('home.html.jinja')  


@app.route('/signup', methods =['GET','POST'])
def signup():  
    if request.method =="POST": 
        username = request.form['username'] 
        email = request.form['email'] 
        password = request.form['password']


        cursor = conn.cursor() 
        cursor.execute(f"INSERT INTO `Users` (Username, Email, Password) VALUES ('{username}', '{email}', '{password}')")

        cursor.close()
        conn.commit()
        


    return render_template('signup.html.jinja')  

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM `Users` WHERE Username = '{username}'")
        user = cursor.fetchone()

        if user and user['Password'] == password: 
            user = load_user(user['ID']) 
            flask_login.login_user(user)
           
            return redirect('/feed')
       
    return render_template('signin.html.jinja')   

@app.route('/feed')
@flask_login.login_required 
def feed(): 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Posts") 
    posts = cursor.fetchall()
    cursor.close()
    
    return render_template('feed.html.jinja', posts=posts) 

@app.route('/post', methods = ['POST'])
def create_post(): 
    description = request.form['description'] 

    cursor = conn.cursor 
    cursor.execute("INSERT INTO `Posts`('description', user_id')")