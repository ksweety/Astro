from flask import Flask, request, render_template
# Importing flask

app = Flask(__name__)   
#Name of 

@app.route('/')
def index(): 
    return render_template('home.html.jinja')  


@app.route('/signup', methods =['GET','POST'])
def signup():  
    if request.method =="POST": 
        username = request.form[username] 
        emailaddress = request.form[emailaddress] 
        password = request.form(password)
        


    return render_template('signup.html')  
