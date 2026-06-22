# if = do some code only if some condition is true else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You're too old to sign up!")
elif age >= 18:
    print("You're now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")   
    
# Example 2

response = input("Would you like food? (Y/N): ")        

if response == "Y":
    print("Here's food for you!")
else:
    print("No food for you!")        
    
# Example 3
name = input("Enter your name: ")    

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")