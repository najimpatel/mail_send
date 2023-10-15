from flask import Flask             # Online pest
# from flask.mail import Mail
from flask_mail import Mail, Message 
# from flask.mail import Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'      #    'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465                       #587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "najimpatel0101@gmail.com"
app.config['MAIL_PASSWORD'] = ""
app.config['MAIL_DEFAULT_SENDER'] = 'Najim'

mail = Mail(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/send')
def send_mail():
    msg = Message("Hello, hi",
                  sender="najimpatel0101@gmail.com",
                  recipients=["hrspatel11112@gmail.com"])
    mail.send(msg)
    return "messege sent!"

if __name__ == '__main__':
    app.run(debug=True)
    