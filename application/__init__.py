import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

# Secret Key config for WTF forms.
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Sendgrid setup.
app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(app)

# Forms


class EmailForm(FlaskForm):
    email = EmailField("Contact email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send email")


# Email Functions // Setup

def send_email(subject, recipient, template):
    msg = Message(subject, recipients=[recipient])
    msg.body = render_template(
        template + ".html")
    msg.html = render_template(
        template + ".html")
    mail.send(msg)

# View Routes


@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = EmailForm()
    email = form.email.data

    if form.validate_on_submit():
        send_email(subject='Testing',
                   recipient=email,
                   template='mail/test')

    return render_template('index.html', form=form)
