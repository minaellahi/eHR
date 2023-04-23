from flask import Flask


#mongo imports
from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


#TASK 01
#pull code from github"
#create "templates" folder in main directory with app.py
#add "home.html" file in "templates". 
#then visit "http://127.0.0.1:8000/"  you will see you home page
#same way create "sigin","signup", "candidate_dashboard", "recruitment_dashboard","candidate_profile" etc
#push code from github



#TASK02
#connect flask app with mongoDB using following code. replace hostname and port with the actual one.
"""client = MongoClient('mongodb://<hostname>:<port>/')
db = client['your_database_name']
"""


if __name__ == '__main__':
    app.run(debug=True)
