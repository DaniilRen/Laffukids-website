from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask_mail import Mail, Message
from payment import create_payment, create_receipt, make_payment
from mail import send_mail


bp = Blueprint('main', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']

		# receipt = create_receipt(name, phone, email)
		# payment = create_payment(receipt)
		# return redirect(payment.confirmation.confirmation_url)
		send_mail(name='Daniil', to='GribnoiChel@yandex.ru')
		return render_template('index.html')

	else:
		return render_template('index.html')


@bp.route('/politics')
def politics():
	return render_template('politics.html')


@bp.route('/oferta')
def oferta():
	return render_template('oferta.html')