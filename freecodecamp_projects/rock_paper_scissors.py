#Key: random.choice function
import random

if __name__ == "__main__":
    while True:
        user = input("What is your choices? r:rock p:paper s:scissors   :")
        computer = random.choice(["r","p","s"])
        try:
            (["r","p","s"].index(user))
        except ValueError: 
            print("Unknown!!! Try again!!!")
            continue
        
        if (user == computer):
            print("It's a tie! One more time!")
        elif ((user == "r" and computer == "s") or
            (user == "p" and computer == "r") or
            (user == "s" and computer == "p")):
            print("You WIN !!!")
            break
        else:
            print("You LOSE !!! Try again?")
        
        
        
        