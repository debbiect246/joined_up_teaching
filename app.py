import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

#building urls for endopoints below
# url for home page

@app.route('/')
def index():
    return render_template('index.html')

#url for psychology of teaching page
 
@app.route('/psychteaching/')
def psychteaching():
    return render_template('psychteaching.html')
    
#url for stress page

@app.route('/stress/')
def stress():
    return render_template('stress.html')

#url for admnin page
@app.route('/admin/')
def admin():
    return render_template('/admin/')

#url for contact page
@app.route('/contact/')
def contact():
    return render_template('/contact/')

#url for blog page
@app.route('/blog/')
def blog():
    return render_template('/blog/')

if __name__ =='__ main__':
    app.run
