import requests


url = "http://localhost:8000/orders"  # or sandbox URL if needed

headers = {
    "Authorization": "Bearer <YOUR_TOKEN>",
    "accept": "application/json",
    "content-type": "application/json",
}

payload = {
    "reference_id": "6a45813f-2d11-4a4b-a91c-8cfe49862858",
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
    "customer_modifiable": True,
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
        "address_modifiable": True
    },
    "redirect_url": "https://pagseguro.uol.com.br",
    "return_url": "https://pagseguro.uol.com.br",
    "notification_urls": [
        "https://pagseguro.uol.com.br"
    ]
    
}

def main():
  response = requests.post(url, headers=headers, json=payload)

  print(response.status_code)
  print(response.json())