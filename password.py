password = "12345"
guess = input("Enter your password")
if guess != password:
    print("Sorry, your password is incorrect")
if guess == password:
    print("Your password is correct")