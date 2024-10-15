import uuid
import os
from flask import Blueprint
from yookassa import Payment
from yookassa import Webhook
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt, ReceiptItem
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder
from yookassa import Configuration


bp = Blueprint('email', __name__, url_prefix="/payment")


# создание квитанции
def create_receipt(name, phone, email):
	Configuration.account_id = os.getenv('YOOKASSA_ACCOUNT_ID')
	Configuration.secret_key = os.getenv('YOOKASSA_SECRET_KEY')
	
	receipt = Receipt()
	receipt.customer = {"name": name, "phone": phone, "email": email}
	receipt.tax_system_code = 1

	receipt.items = [
		ReceiptItem({
			"description": "Collection of recipes",
			"quantity": 1.0,
			"amount": {
					"value": 349.0,
					"currency": Currency.RUB
			},
			"vat_code": 2
		})
	]
	return receipt


# создание платежа на основе квитанции и получение данных
def create_payment(receipt, conf_type=ConfirmationType.REDIRECT):
	idempotence_key = str(uuid.uuid4())
	builder = PaymentRequestBuilder()
	builder.set_amount({"value": 349, "currency": Currency.RUB}) \
		.set_confirmation({"type": conf_type, "return_url": "https://lafukids.ru"}) \
		.set_capture(True) \
		.set_description("Cборник рецептов") \
		.set_metadata({
			"customer_name": receipt.customer.name,
			"customer_email": receipt.customer.email,
			"customer_phone": receipt.customer.phone
			}) \
		.set_receipt(receipt)

	request = builder.build()
	payment = Payment.create(request, idempotence_key)
	return payment
