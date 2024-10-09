import uuid
from yookassa import Payment
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.receipt import Receipt, ReceiptItem
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.request.payment_request_builder import PaymentRequestBuilder


# создание квитанции
def create_receipt(name, phone, email):
	receipt = Receipt()
	receipt.customer = {"name": name, "phone": phone, "email": email}
	receipt.tax_system_code = 1

	receipt.items = [
		ReceiptItem({
			"description": "Collection of recipes",
			"quantity": 2.0,
			"amount": {
					"value": 650.0,
					"currency": Currency.RUB
			},
			"vat_code": 2
		})
	]
	return receipt


# создание платежа на основе квитанции и получение данных
def create_payment(receipt):
	idempotence_key = str(uuid.uuid4())
	builder = PaymentRequestBuilder()
	builder.set_amount({"value": 650, "currency": Currency.RUB}) \
		.set_confirmation({"type": ConfirmationType.REDIRECT, "return_url": "http://127.0.0.1:5000/"}) \
		.set_capture(False) \
		.set_description("Заказ Сборника") \
		.set_metadata({"orderNumber": "72"}) \
		.set_receipt(receipt)

	request = builder.build()
	# request.client_ip = '1.2.3.4'
	payment = Payment.create(request, idempotence_key)

	return payment
	

# создание платежа получение данных
def make_payment():
	idempotence_key = str(uuid.uuid4())
	payment = Payment.create({
		"amount": {
			"value": "650.00",
			"currency": "RUB"
		},
		"payment_method_data": {
			"type": "bank_card"
		},
		"confirmation": {
			"type": "redirect",
			"return_url": "http://127.0.0.1:5000/"
		},
		"description": "Заказ №72"
	}, idempotence_key)

	return payment