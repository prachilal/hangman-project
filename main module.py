import listofsecretwords
import random
ln = 1
count = 0
nw = []
if ln == 1: #ln: list number
    print ("hint: the word is a name of a fruit")
    l = (listofsecretwords.l1).copy()
    wc = random.randrange(0,len(listofsecretwords.l1))    #wc: word choice
else:
    print ("hint: the word is a name of a vehicle")
    l = (listofsecretwords.l2).copy()
    wc = random.randrange(0,len(listofsecretwords.l2))

word = l[wc]

wcc = len(word) #wcc: word choice count

for i in range(0,len(l)+1):
    nw.insert(i,"_")
print (nw)

for i in range (1,len(l)+3):
    lg = input("enter a letter guess:") #lg: letter guess
    if lg in word:
        count = count + 1
        x = word.index(lg)
        for i in range (0,wcc):
            if i == x:
                nw[i] = lg
                print(nw)          
    else :
        print ("sorry try again")
    if count == wcc:
        print("you guessed it correct")
        break
    
    
    
