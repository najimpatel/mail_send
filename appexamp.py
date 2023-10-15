from flask import Flask
import email_to


app = Flask(__name__)


@app.route('/')
def index():

    server = email_to.EmailServer('smtp.gmail.com', 587, 'najimpatel0101@gmail.com', 'NPpassword')
    server.quick_email('hrspatel11112@gmail.com', 'Test',
                   ['# A Heading', 'Hi Hope you are good!'],
                   style='h1 {color: blue}')

    return 'Message sent!'


if __name__ == '__mail__':
    app.run(debug=True)
