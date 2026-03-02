print(True and False) #false
print(True and True)  #true
print(False and True) #false
print(False and False) #false
print(True or True) #true
print(True or False) #true
print(False or False) #false
print(False or True) #true

True and False or False or True and True and False or True
#True


people_in_the_house = int(input('enter how many people are in the house:'))
family_member = int(input('family members quantity:'))
thief_detected = people_in_the_house > family_member
print(thief_detected)