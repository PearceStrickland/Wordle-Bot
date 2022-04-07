import random 

#Reading file and pulling random word for solution
with open("Wordle_Solutions.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
solution=random.choice(words)
answer=False 
guess_number=1
while answer==False:
    places=""
    guess=input(str(guess_number)+" guess: ")
    with open('Wordle_PossibleGuesses.txt') as file:
        contents = file.read()
    if len(guess)==5:    
        if guess in contents:
            for i in range(5):
                if guess[i] in solution:
                    if guess[i]==solution[i]:
                        places+="2"
                    else:
                        places+="1"
                else:
                    places+="0"
        else:
            print ('Invalid Guess')
            continue
    else:
        print ('Invalid Guess')
        continue
    print(guess)
    print(places)
    guess_number+=1
    if places=="22222":
        print("You got it!")
        answer=True

