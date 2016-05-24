from flask import Flask
from app import mail

app = Flask(__name__, template_folder='template')
app.config.from_object(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'hub25flow@gmail.com'
app.config["MAIL_PASSWORD"] = 'thehub254'


mail.init_app(app)

