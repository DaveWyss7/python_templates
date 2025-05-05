"""
Unpacking a list in Python
"""
product_infos = [
    'Chrome Boo§k 15.0.874.121',
    'Electronis',
    'Black',
    'Laptop',
    1329.99,
    'In Stock',
    ]

product_name, *_, price, available = product_infos

print(f'{product_name} costs ${price} and is {available}')
