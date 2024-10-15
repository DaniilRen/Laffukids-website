from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify
from flask_mail import Mail, Message
from payment import create_payment, create_receipt
from mail import send_mail


bp = Blueprint('main', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']

		receipt = create_receipt(name, phone, email)
		payment = create_payment(receipt)
		return redirect(payment.confirmation.confirmation_url)
		
	else:
		return render_template('index.html')


@bp.route('/politics', methods=("GET", "POST"))
def politics():
	return render_template('politics.html')



@bp.route('/oferta', methods=("GET", "POST"))
def oferta():
	return render_template('oferta.html')


# обработка платежей
@bp.route('/payment_notification', methods=("GET", "POST"))
def payment_notification():
	try:
		event = request.json["event"]
		payment = request.json["object"]
		if event == "payment.succeeded" and payment["status"] == "succeeded":
			print("Sending mail...")
			send_mail(name=payment["metadata"]["customer_name"], to=payment["metadata"]["customer_email"])
			resp = "success"
		else:
			resp = "wrong request data"
	except Exception as e:
		resp = e
	return "", 200