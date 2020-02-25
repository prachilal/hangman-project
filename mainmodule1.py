import listofsecretwords
import random


ln = random.randint(0,1)


if ln == 1: #ln: list number
    print ("hint: the word is a name of a fruit")
    l = (listofsecretwords.l1).copy()
    word = l[random.randrange(0,len(listofsecretwords.l1))] 
else:
    print ("hint: the word is a name of a vehicle")
    l = (listofsecretwords.l2).copy()
    word = l[random.randrange(0,len(listofsecretwords.l2))]

print("number of words:",len(word))
turns = len(word)+1

guesses = input("make a guess")

while (turns > 0):

    failed = 0

    
    
    for char in word:
        if char in guesses:
             print(char)
        else:
            print("_")
            failed = failed +1

    if failed == 0:
        print("you win")
        break

    if (turns == 0):
        print("you loose")

    guess = input("guess a letter")
    guesses = guesses+guess

    if guess not in word:
        print("try again")
        turns = turns -1
        print("number of turns:",turns)

    if turns == 0:
        print("you loose")


print("the word is:", word)

        
         
        
        
