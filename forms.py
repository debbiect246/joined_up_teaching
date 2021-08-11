from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.Required()])
    email = TextField("Email", [validators.Required(), validators.Email()])
    subject = TextField("Subject", [validators.Required()])
    message = TextAreaField("Message", [validators.Required()])
    submit = SubmitField("Send")

#above creates a form
#imported form class from wtf forms,
#created each field on the form
#validators added
#imported validators and validation error library
#used pip install flask email_validator to install email validator

