from flask import Flask, render_template
# Importing flask

app = Flask(__name__)   
#Name of 

@app.route('/')
def index(): 
    return render_template('home.html.jinja')  


@app.route('/signup')
def signup(): 
    return render_template('signup.html')  
