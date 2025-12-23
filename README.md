{
	"id": "CHEC_120301FA-8B8B-4C25-B07D-A4541EB78EB5",
	"reference_id": "6a45813f-2d11-4a4b-a91c-8cfe49862858",
	"expiration_date": "2023-06-14T21:45:00-03:00",
	"created_at": "2023-06-14T15:45:00-03:00",
	"status": "INACTIVE",
	"customer": {
		"name": "joao",
		"email": "joao@joao.com",
		"tax_id": "00000000000",
		"phone": {
			"country": "+55",
			"area": "27",
			"number": "999999999"
		}
	},
	"customer_modifiable": true,
	"items": [
		{
			"reference_id": "123",
			"name": "Compra Checkout Pagbank",
			"quantity": 1,
			"unit_amount": 500,
			"dimensions": {
				"length": 1234,
				"width": 10,
				"height": 12345
			},
			"weight": 10,
			"image_url": "https://www.google.com"
		}
	],
	"additional_amount": 0,
	"discount_amount": 0,
	"shipping": {
		"type": "FREE",
		"service_type": "PAC",
		"amount": 0,
		"address": {
			"country": "BRA",
			"region_code": "SP",
			"city": "São Paulo",
			"postal_code": "01452002",
			"street": "Faria Lima",
			"number": "1384",
			"locality": "Pinheiros",
			"complement": "5 andar"
		},
		"address_modifiable": true
	},
	"redirect_url": "https://pagseguro.uol.com.br",
	"return_url": "https://pagseguro.uol.com.br",
	"notification_urls": [
		"https://pagseguro.uol.com.br"
	],
	"links": [
		{
			"rel": "PAY",
			"href": "https://pagamento.pagseguro.uol.com.br/pagamento?code=xxxx",
			"method": "GET"
		},
    {
			"rel": "SELF",
			"href": "https://api.pagseguro.com/checkouts/CHEC_xxxx",
			"method": "GET"
		},
		{
			"rel": "INACTIVATE",
			"href": "https://api.pagseguro.com/checkouts/CHEC_xxxx/activate",
			"method": "POST"
		}
	]
}