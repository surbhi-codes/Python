# Strings   
first_name = "Surbhi"
favourite_food = "Momos"
email = "surbhi@diva.com"
"""
print(f"Hello {first_name}")
print(f"You like {favourite_food}")
print(f"Your email is {email}")
"""
# Integers
age = 22
quantity = 3
num_of_students = 50

print(f"You're {age} years old") 
# The f in Python stands for “formatted string” (or f-string) It lets you directly insert variables or expressions inside a string- cleanly and efficiently.
# Without f, Python treats everything inside quotes as plain text
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float
price = 10.99
gpa = 9.5

print(f"The price is ${price}")
print(f"Your gpa is :{gpa}")

#Boolean

is_student = True
print(f"Are you a student?: {is_student}")

is_online = False
if is_online:
    print("You're online")
else: 
    print("You're offline")
