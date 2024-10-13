from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify
from flask import make_response
from flask_mail import Mail, Message
from payment import create_payment, create_receipt, check_id
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

		# send_mail(name=name, to=email)

	else:
		return render_template('index.html')


@bp.route('/politics', methods=("GET", "POST"))
def politics():
	return render_template('politics.html')


@bp.route('/oferta', methods=("GET", "POST"))
def oferta():
	return render_template('oferta.html')



@bp.route('/payment-notification', methods=("GET", "POST"))
def payment_notification():
	try:
		event = request.args.get("event", default=None)
		payment = request.args.get("object", default=None)
		if event == "payment.succeeded " and check_id(payment.id):
			send_mail(payment.metadata.customer_email)
			return make_response(f"Success for event: {event}", status_code=200) 
		error = "Wrong payment id or status"
	except Exception as e:
		error = e
	return make_response(f"Error: {error} for event: {event}", status_code=500) 