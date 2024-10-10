from flask import Flask
import os
from dotenv import load_dotenv
from flask import render_template
from flask import redirect
from flask import request
from payment import create_payment, create_receipt, make_payment
from yookassa import Configuration


app = Flask(__name__)

# yookassa config
Configuration.account_id = '467956'
Configuration.secret_key = 'test_Yf2ocwOYQBDf1P7VRXW-exqxyMmmL4Zo8BOzQsaYnWA'


@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']

		# payment = make_payment()
		receipt = create_receipt(name, phone, email)
		payment = create_payment(receipt)
		return redirect(payment.confirmation.confirmation_url)

	else:
		return render_template('index.html')


@app.route('/politics')
def politics():
	return render_template('politics.html')


@app.route('/oferta')
def oferta():
	return render_template('oferta.html')


if __name__ == "__main__":
	load_dotenv()
	Configuration.account_id = os.getenv('YOOKASSA_ACCOUNT_ID')
	Configuration.secret_key = os.getenv('YOOKASSA_SECRET_KEY')
	print(os.getenv('YOOKASSA_ACCOUNT_ID'))
	print(os.getenv('YOOKASSA_SECRET_KEY'))

	app.run()