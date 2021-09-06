from collections import Counter

phones = ['Iphone', 'Samsung', 'LG', 'Iphone', 'LG']

count = Counter(phones)
print(count['Hello'])

text = 'Ехал Грека через реку видит Грека в речке рак'.lower().replace(' ','')
count = Counter(text)
print(count)