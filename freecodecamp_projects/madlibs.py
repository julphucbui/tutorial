# Key: string format functions
# https://www.youtube.com/watch?v=8ext9G7xspg
import random

sentence1 = '''
Hi {}! Nice to meet you.
It's great to hear that you also like {}.
I've met {} once. That was amazing!
'''

sentence2 = '''
Hi %s! Welcome to Madlibs project.
It's great to hear that you also like %s.
I've met %s once. That was amazing!
'''

if __name__ == "__main__":
    name = input('Name: ')
    favorite_sport = input('Favorite sport: ')
    favorite_player = input('Favorite player: ')
    ranNum = random.randint(1,3)
    
    if ranNum == 1:
        #solution 1
        msg = sentence1.format(name,favorite_sport,favorite_player)
    elif ranNum == 2:
        #solution 2
        msg = f"Hello {name}! Nice to meet you.\nIt's great to hear that you also like {favorite_sport}.\nI've met {favorite_player} once. That was amazing!"
    elif ranNum == 3:
        #solution 3
        msg = sentence2 % (name,favorite_sport,favorite_player)
    else:
        msg = "Oops! Something went wrong!!!"

    print(msg)