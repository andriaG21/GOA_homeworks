# type() - ფუნქცია გვიჩვენებს რომ გავიგოთ ცვლადში რომელი მონაცემთა ტიპია შეტანილი.

name = 'andria'
last_name = 'guramishvili'
age = 13
num = 7.5
num_2 = 65
print(type(name))
print(type(last_name))
print(type(age))
print(type(num))
print(type(num_2))


name1 = 'andria'
lastname1 = 'guramishvili'
age1 = '13'
print('i am' + name1 + lastname1 + 'and i am' + age1 + 'years old')

f1 = float(input('enter num :'))
f2 = float(input('enter num :'))
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)


n1 = float(input('enter num1 :'))
n2 = float(input('enter num2 :'))
n3 = float(input('enter num3 :'))
n4 = float(input('enter num4 :'))
n5 = float(input('enter num5 :'))

avg = (n1 + n2 + n3 + n4 + n5) /5
print(avg)


c = int(input('enter temp :'))
f = c * 1.8 + 32
print(f)

f = int(input('enter temp :'))
c = (f-32)*1.8
print(c)
