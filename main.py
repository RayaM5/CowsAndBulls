import random
listn = []

def Makenum ():
    for n in range(4):
        num12=random.randrange(0,9)
        listn.append (num12)
    if len(listn)> len(set(listn)):
        listn. clear()
        Makenum()
        

def game(numd):
     count= 0

    while True:
            guess = [int(i) for i in str(input("Please guess 4-digit number: "))]
            while True:
                len(guess) < len(set(guess)):
                guess. clear()
                guess = [int(i) for i in str(input("Please guess 4-digit number: "))]
               
            if guess == listn:
                print("You won.")
                print("It took you "+str(count)+" guess(es).")
                break
            
            elif count >= 10:
                print (str(listn))
                break
                
            else:
                cow=0
                bull=0
                for x in range(0,numd):
                    if guess[x]==listn[x]:
                        bull += 1
                    elif guess[x] in listn:
                        cow += 1

            print("Cows: "+str(cow)+" Bulls: "+str(bull))



Makenum()
print (str(listn))
game(4)