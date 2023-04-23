from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#pull code from github"
#create "templates" folder in main directory with app.py

#add "home.html" file in "templates". 
#then visit "http://127.0.0.1:8000/"  you will see you home page
#same way create "sigin","signup", "candidate_dashboard", "recruitment_dashboard","candidate_profile" etc
#push code from github



if __name__ == '__main__':
    app.run(debug == 'True')
