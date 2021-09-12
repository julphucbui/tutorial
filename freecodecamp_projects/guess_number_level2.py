import random
import csv

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

def get_highscores():
    try:
        with open('./guess_number_high_score.csv', newline='') as f:
            reader = csv.reader(f)
            list_highscores = list(reader)
    except Exception as e:
        pass

    return list_highscores

def save_highscores(list_highscores):
    with open('./guess_number_high_score.csv', 'w', newline="") as f: 
        write = csv.writer(f)
        write.writerows(list_highscores)

def show_highscores(list_highscores):
    #format: '{message:{fill}{align}{width}}'
    disp = "{:20}|{}".format("Name","Tries")
    for a_highscore in list_highscores:
        disp = disp + "\n{:20}|{}".format(a_highscore[0],a_highscore[1])
    print(disp)

def sort_highscores(a_highscore):
    return int(a_highscore[1]) #sort by try count

################ MAIN ################
if __name__ == "__main__":
    minNum, maxNum = 1, 100
    your_name = input("Name: ")
    tried_cnt = 0
    my_number = random.randint(minNum,maxNum)
    #print(my_number)
    try:
        list_highscores = get_highscores()
    except Exception as e:
        pass

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
                list_highscores.insert(0,[your_name,tried_cnt])
                list_highscores.sort(key=sort_highscores)
                show_highscores(list_highscores)
                save_highscores(list_highscores)  #skip title
                break
        except Exception as e:
            print(e)
