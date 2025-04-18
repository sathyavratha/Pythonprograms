#normal guessing game where user enters a word until its the secret word
#lets set a limit user should try to guess within
secret_word="Elephant"
guess = ""
limit = 0
while guess != secret_word:
    guess = input("Guess a word! :")
    limit +=1
    if limit > 3 :
        print("Oops! You've used all your chances")
        print("If you wish to know the secret word type Reveal!")
        reveal=input()
        if reveal =='Reveal':
            print(secret_word)

print("You win!!!")
