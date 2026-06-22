# Typecasting = the process of converting a variable from one data type to another. str(), int(), float(), bool()

name = "Surbhi"
age = 22
gpa = 9.5
is_student = True

print(type(gpa)) # shows type → <class 'float'>

gpa = int(gpa)  # converts 9.5 → 9 
print(gpa)      # prints 9

"""
age = float(age)
print(age)
"""

age = str(age)
age += "1"  #joins "22" + "1" → "221" Python does NOT allow adding number + text
print(age)