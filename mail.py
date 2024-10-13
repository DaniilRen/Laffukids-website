# from threading import Thread
from flask import Blueprint
from flask import current_app
from flask_mail import Message
from flask_mail import Mail
from time import sleep    

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl


bp = Blueprint('mail', __name__, url_prefix="/mail")


def send_mail(name, to):
	app = current_app._get_current_object()
	mail = Mail(app)
	msg = Message(subject="Сборник рецептов", sender=("Laffy kids",app.config["MAIL_DEFAULT_SENDER"]), recipients=[to])
	msg.body = f"{name}, Благодарим вас за покупку нашего сборника! Файл прикреплен к данному письму."
	with app.open_resource("static/recipes.pdf") as fp:
		msg.attach(filename="recipes.pdf", disposition="attachment", content_type="application/pdf", data=fp.read())
	mail.send(msg)
	print("Mail has been sent to", name, to)