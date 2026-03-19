# 1

int = int(input('enter integer :'))
if int > 0:
    print('positive')
elif int < 0:
    print('negative')
else:
    print('zero')

# 2

correct_pas = 'python123'
password = input('enter password :')
while password != correct_pas:
    password = input('enter password :')
if password != correct_pas:
    print('wrong password, try again')
else:
    print('access granted')

# 3

fruits = ['banana', 'apple', 'orange', 'mango', 'cherry']
print(fruits[1], fruits[2], fruits[4])