# Rock Papper Scissor game
import random

print("0) Rock")
print("1) papper")
print("2) scissor")
user_choice = int(input("choose a number (0-2) >>  "))
if user_choice >= 3 and user_choice < 0:
    print("invalid please choose valid ") 
else:
    print("Rock")
    print("my choice is ", user_choice)
    Ai_choice = random.randrange(0,3)
    print("Ai choice is " , Ai_choice)
    if user_choice == Ai_choice:
        print("game Draw ")
    elif user_choice == 0 and Ai_choice == 1:
        print(" Ai won the game ")
    elif user_choice == 1 and Ai_choice == 0:
        print("You won the game ")
    elif user_choice == 1 and Ai_choice == 2:
        print("Ai won the game")
    elif user_choice == 2 and Ai_choice == 1:
        print("you won the game")
    elif user_choice == 2 > Ai_choice == 0:
        print("Ai won the game")
    elif user_choice == 0 < Ai_choice == 2:
        print("you won the game")
print("Thank you ")