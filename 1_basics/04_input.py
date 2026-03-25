# input() = A function that prompts the user to enter data
#  Returns the entered data as a string

name = input("What's your name?: ")
age = int(input("How old are you?: ")) #int() → converts that string into integer (number)

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You're {age} years old")