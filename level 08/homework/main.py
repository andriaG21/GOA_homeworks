# 2) comparison operations - შედარების ოპერატორები

# > - მეტია
# < - ნაკლებია
# >= - მეტია ან ტოლია
# <= - ნაკლებია ან ტოლია
# == - უდრის (ის ამოწმებს მონაცემს და მონაცემთა ტიპს)
# != - არ უდრის (ის ამოწმებს მონაცემს და მონაცემთა ტიპს)

# >
print(33>27)
print(81>82)

# <
print(59<76)
print(63<87)

# >=
print(43>=65)
print(18>=18)

# ==
print(23==48)
print(72==72)

# !=
print(53!=53)
print(23!=89)


# 3) logical operations - ლოგიკური ოპერატორები

# and - და (მკაცრი ოპერატორი)
# or - ან (არამკაცრი ოპერატორი)
# and - ორივე თუ true არის იქნება true, ერთ-ერთი თუ false არის იქნება false
# or - ერთ-ერთი თუ true არის იქნება true, ორივე თუ false არის იქნება false


# 4)

your_height = float(input('enter your height :'))
my_height = 1.60
print(your_height > my_height)


# 5) რატომ გამოიტანს code false-ს ტერმინალში

num1 = '21'
num2 = 21
print(num1 == num2)
# იმიტომ გამოვა ტერმინალში false რადგან პირველ ცვლადში შენახულია string, ხოლო მეორეში integer და ისინი ერთმანეთს არ უდრიან


# 6) 

my_surname = 'guramishvili'
your_surname = input('enter your surname :')
print(my_surname == your_surname)


# 7) რას გამოიტანს

# false or true and true and false
# false or false: false

# true and false or false or true
# false or true: true

# true or true and false or true or false and true or false
# true or false or true or false or false: true


# 8)

temprature = int(input('enter temprature :'))
co_sistem = temprature > 30
print(co_sistem)


# 9)

# მომხმარებელი შეჰყავს ტემპერატურა ცელსიუსში
celsius = float(input("enter room temprature (°C): "))

# ცელსიუსიდან ფარენგეიტში გადაყვანის ფორმულა
fahrenheit = celsius * 9/5 + 32

print("temprature is:", fahrenheit)

# თუ ტემპერატურა 89.6°F-ს აჭარბებს, სისტემა ჩაირთვება
print(fahrenheit > 89.6)