from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(  

      #EMAIL SETTINGS  

     MAIL_SERVER='smtp.qq.com',  

     MAIL_PORT=465, 

     MAIL_USE_SSL=True, 

    MAIL_USERNAME = '373391120',

     MAIL_PASSWORD = 'gfjyffuwekeccagh'    )




mail = Mail(app)

@app.route("/")
def index():  

     msg = Message(subject="helloworld", sender='373391120@qq.com', recipients=['469372483@qq.com'])

     msg.html = "testinghtml"  

     mail.send(msg)
     return 'helolo'


if __name__ =='__main__':

    app.run(debug=True)

