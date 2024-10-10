from flask import Flask
import main, mail, payment
from dotenv import load_dotenv
from yookassa import Configuration
import os


def create_app():
	# yookassa config
	Configuration.account_id = os.getenv('YOOKASSA_ACCOUNT_ID')
	Configuration.secret_key = os.getenv('YOOKASSA_SECRET_KEY')

	# flask app config
	app = Flask(__name__)

	app.register_blueprint(main.bp)
	app.register_blueprint(mail.bp)
	app.register_blueprint(payment.bp)

	# app.add_url_rule("/", endpoint="index")

	load_dotenv()

	app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
	app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
	app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'False').lower() == 'true'
	app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
	app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
	app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
	
	return app