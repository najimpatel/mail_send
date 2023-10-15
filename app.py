from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


# mail = Mail(app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'jxkalmhefacbuk@gmail.com'
# app.config['MAIL_PASSWORD'] = 'kelvin7322'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'   #'smtp.googlemail.com'
app.config['MAIL_PORT'] =   587            # 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'najimpatel0101@gmail.com'
app.config['MAIL_PASSWORD'] = ''
# app.config.from_pyfile('config.cfg')

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello harsh bro', 
                    sender='jxkalmhefacbuk@gmail.com',
                    recipients = ['najimpatel0101@gmail.com'] )
    mail.send(msg)
    return 'Message sent!'


if __name__ == '__mail__':
    app.run(debug=True)



# from distutils.log import debug
# from email.message import Message
# from pickle import TRUE