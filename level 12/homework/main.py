num = int(input('enter int: '))
if num % 2 == 0:
    print('even')
else:
    print('odd')

temtrature = int(input('enter temprature: '))
if temtrature > 30:
    print("it's hot")
elif temtrature > 14 < 31:
    print("it's warm")
else:
    print("it's cold")

num1 = int(input('enter number: '))
if num1 > 0:
    if num1 % 2 == 0:
        print('positive even')
    else:
        print('positive odd')
else:
    print('negative')

num2 = int(input('enter the number: '))
for i in range(0,num,1):
    if i % 2 == 0:
        print(i, '- even')
    else:
        print(i, '- odd')

positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input(f"enter {i+1} number: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("positive:", positive)
print("negative:", negative)
print("zeros:", zero)

fruits = ["apple", "banana", "orange", "grape"]
fruits [1] = 'kiwi'
print(fruits)

nums = [4, 8, 12, 16, 20]
print(nums[0] + nums[4])

cities = ['barcelona', 'madrid', 'munich', 'bali', 'washington']
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
print(cities[4])

int = [3, 14, 12, 67, 34, 23, 26]
print(int[1])
print(int[2])
print(int[4])
print(int[6])

print(int[1] + int[2] + int[4] + int[6])

integer = [4, 18, 6, 62, 1, 7]
print(integer[1])
print(integer[3])
print(integer[5])

name = 'andria'
print(name[0], name[1], name[2], name[3], name[4], name[5])

animals = ['dog', 'cat', 'snake', 'bear','lion', 'horse', 'pig']
print(animals[0], animals[1], animals[2])