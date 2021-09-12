#KEY: random function and string format functions
import random

def get_message(tried_cnt):
    msg = ""
    if tried_cnt == 1:
        msg = "HEAD SHOT!!!"
    elif tried_cnt < 6:
        msg = f"Amazing! You found it just after {tried_cnt} try."
    elif tried_cnt < 10:
        msg = f"Not bad! You found it after {tried_cnt} try."
    else:
        msg = f"Thanks God! You finally found it after {tried_cnt} try."
    return msg

################ MAIN ################
if __name__ == "__main__":
    minNum, maxNum = 1, 100
    your_name = input("Name: ")
    tried_cnt = 0
    my_number = random.randint(minNum,maxNum)
    while True:
        tried_cnt = tried_cnt + 1
        your_number_str = input(f"Guess a number from {minNum} to {maxNum}:     ")
        try:
            your_number = int(your_number_str)
            if my_number > your_number:
                print("No. My number is larger. Try again!")
            elif my_number < your_number:
                print("No. My number is smaller. Try again!")
            else:
                print(f"Congratulation {your_name}! " + get_message(tried_cnt))
                break
        except Exception as e:
            print("Oops! It seems not to be a number? Try again!")
