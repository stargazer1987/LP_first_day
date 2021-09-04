a = 2
b = 0.5
print(a + b)
name = "Женя"
print(f'Привет {name}')
print(float('1'))
#print(int('2.5')) # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1))
print(bool(''))
print(bool(0))


myList = [3, 5, 7, 9, 10.5]
print(myList)
myList.append('Python')
print(len(myList))
print(myList[0])
print(myList[-1])
print(myList[1:])
myList.remove('Python')
print(myList)


myDict = {'city': 'Москва', 'temperature': 20}
print(myDict['city'])
myDict['temperature'] += 5
print(myDict)
print(myDict.get('country'))
print(myDict.get('country', 'Россия'))
myDict['data'] = '27.05.2019'
print(len(myDict))
