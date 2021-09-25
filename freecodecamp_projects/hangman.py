import random


if __name__ == "__main__":
    HIDDEN_STR = "_"
    #1. words preparation
    with open("./hangman_words.txt", "r") as f:
        words = f.readlines()
    word_to_guess = random.choice(words).strip("\n").upper()
    word_cnt = len(word_to_guess)
    current_guess_word = HIDDEN_STR * word_cnt
    hidden_word_cnt = current_guess_word.count(HIDDEN_STR)
    print(word_to_guess)
    #2. start the game
    print("Welcome to hangman game!")
    while True:
        print(current_guess_word)
        guess_str = input("The word has %d letter%s \n"%(word_cnt, "s" if word_cnt > 1 else ""))
        guess_str = guess_str[0].upper()  #just accept 1 letter. 
        #3. Check guess_str 
        cnt = 0
        for i in range(0, word_cnt):
            if word_to_guess[i] == guess_str:
                cnt = cnt + 1
                current_guess_word = current_guess_word[:i] + guess_str + current_guess_word[i+1:] 
        
        #4. Show the result
        hidden_word_cnt = current_guess_word.count(HIDDEN_STR)
        if hidden_word_cnt == 0:
            #End game
            print("Congratulation!!! All done")
            break
        elif cnt != 0:
            print("Good job! You found {} letter{} {}".format(cnt,"s" if cnt > 1 else "",guess_str))
        else:
            print("Oops! It is not in the word\n")
        