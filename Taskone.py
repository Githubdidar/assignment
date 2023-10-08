mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'}, #0
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'}, #1
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 107.25
            }
for item in mobile_data['data']:
    price_usd = float(item['price'].split()[0])

    bdt_price = price_usd * mobile_data['exchange_rate']

    item_name = item['name']

    item_made = item['made']

    template = f"{item_name} is made in {item_made}. The price is {price_usd} which is almost equal to {bdt_price} BDT."

    print(template)



# Make a template using the dictionary data.
# Your Template must have at least two sentences.
# USD must be converted to BDT
# example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT



