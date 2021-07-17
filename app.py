import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

#building urls for endopoints below
# url for home page

@app.route('/')
def index():
    return render_template('index.html', title="Home")

#url for psychology of teaching page
#adding title to render template puts title of page on screen
 
@app.route('/psychteaching/')
def psychteaching():
    return render_template('psychteaching.html', title="Psychology of Teaching")
    
#url for stress page

@app.route('/stress/')
def stress():
    return render_template('stress.html', title = "Dealing with Stress")

#url for admnin page
@app.route('/admin/')
def admin():
    return render_template('admin.html', title = "Managing Admin")

#url for contact page
@app.route('/contact/')
def contact():
    return render_template('contact.html', title= "Contact Me")

#url for blog page
@app.route('/blog/')
def blog():
    return render_template('blog.html', title = "Blog")

if __name__ =='__ main__':
    app.run
