from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '3ce1dd8de8334b14a49931fbf365ffda'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.db"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_USERNAME'] = '235harsh@gmail.com'
# app.config['MAIL_PASSWORD']= os.environ.get('EMAIL_PASS')
app.config['MAIL_PASSWORD']= 'frhchzmmopcbhvus'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'



mail = Mail(app)