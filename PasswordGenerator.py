#password genrator
import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B"
           "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["!","@","#","$","%","^","&","*","(",")","_","+"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

print("Welcome to the password generator")
user_letters = int(input("How many letters would you like in your password? "))
user_symbols = int(input("How many symbols would you like in your password? "))
user_numbers = int(input("How many numbers would you like in your password? "))

password_letters = random.choices(letters, k=user_letters)
password_symbols = random.choices(symbols, k=user_symbols)
password_numbers = random.choices(numbers, k=user_numbers)

password = password_letters + password_symbols + password_numbers
random.shuffle(password)

print("Your password is: " + "".join(password))
