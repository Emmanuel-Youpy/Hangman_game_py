import random
name = input ('Please enter Your name:\n')
print("Welcome to kazeem Hangman Game ")
print("Goodluck !", name)
print("guess the character")
def hang():
    # set of varibles list
    country = ["nigeria", "italy", "france", "england", "qatar"]
    building = ["house", "stadium", "hotel", "school", "mosque"]
    city = ["lagos", "newyork", "milan", "london", "paris"]
    choice = (random.choice(country), random.choice(building), random.choice(city))
    word = random.choice(choice)
    print("This word is ", len(word), " letters long")
    count = 4
    guesses =''
    while count > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_')
                failed +=1
        if failed == 0:
            print("You Win")
            print("the word is: \n",word)
            break

        guess = input("guess a character: \n")
        guesses += guess
        if guess not in word:
            count -=1
            print("Wrong")
            print('you have',count,'more guesses')
        if count ==0:
            print("you Loose","game over")

hang()