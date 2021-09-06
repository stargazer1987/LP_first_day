balance = 50
price = 10

if balance > price:
    print('Спасибо за покупку')
else:
    print('Пополните баланс!')


def weather(temperature):
    if temperature <= 0:
        return('На улице холодно')
    elif 0 < temperature < 15:
        return('На улице прохладно')
    elif 15 <= temperature < 25:
        return('На улице тепло')
    else:
        return('На улице жарко')

print(weather(2))
print(weather(-2))
print(weather(20))
print(weather(12))
print(weather(30))

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 80}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower() or not name :
        return price
    else:
        return price - (price * discount / 100)

apple_desc = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(apple_desc)

androind_desc = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
print(androind_desc)

noname_desc = discounted(phone3['price'], phone3['discount'], name=phone3['name'])
print(noname_desc)