# from threading import Thread
from flask import Blueprint
from flask import current_app
from flask_mail import Message
from flask_mail import Mail
from time import sleep    


bp = Blueprint('mail', __name__, url_prefix="/mail")


# def send_async_email(app, msg):
# 	with app.app_context():
# 		mail = Mail(app)
# 		# block only for testing parallel thread
# 		for i in range(10, -1, -1):
# 			sleep(2)
# 			print('time:', i)
# 		print('====> sending async')
# 		mail.send(msg)


# def send_email(name, to):
# 	app = current_app._get_current_object()
# 	msg = Message(subject="Сборник рецептов от @laffykids", sender=app.config["MAIL_DEFAULT_SENDER"], recipients=[to])
# 	msg.body = f"{name}, Благодарим вас за покупку нашего сборник! Файл с рецептами прикреплен ниже в письме."
# 	with app.open_resource("static/recipes.pdf") as fp:
# 		msg.attach(filename="recipes.pdf", disposition="attachment", content_type="application/pdf", data=fp.read())
# 	thr = Thread(target=send_async_email, args=[app, msg])
# 	thr.start()
# 	return thr


def send_mail(name, to):
	app = current_app._get_current_object()
	mail = Mail(app)
	msg = Message(subject="Сборник рецептов от @laffykids", sender=app.config["MAIL_DEFAULT_SENDER"], recipients=[to])
	msg.body = f"{name}, Благодарим вас за покупку нашего сборник! Файл с рецептами прикреплен ниже в письме."
	with app.open_resource("static/recipes.pdf") as fp:
		msg.attach(filename="recipes.pdf", disposition="attachment", content_type="application/pdf", data=fp.read())
	mail.send(msg)
	print("Mail successfully sent to", name, to)
