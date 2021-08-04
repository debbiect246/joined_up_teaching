import os
from flask import Flask, render_template, url_for, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "161 newkey"

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
#links to contactFrom created in forms.py
#remember to call Form class with () brackets or will get a self error!
#use get and post so that information will be posted to server and then onto email.
#hidden tag in form enabling csrf protection.
#render template renders contact template which is displayed on screen.

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm

    if request.method =='POST':
        return 'Form posted.'
    elif request.method =='GET':
        return render_template('contact.html', title= "Contact Us", form=form())

#url for blog page
@app.route('/blog/')
def blog():
    return render_template('blog.html', title = "Blog")

if __name__ =='__ main__':
    app.run
