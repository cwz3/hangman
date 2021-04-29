'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: charles    cwz3
'''



def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    missesLeft=0
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    difficulty=input("(h)ard or (e)asy> ")
    if difficulty=='h':
        missesLeft=8
        return 8
    else:
        missesLeft=12
        return 12
        
def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    import random
   
    lengthwords=[]
    for word in words:
        if len(word)==length:
            lengthwords.append(word)
    
    x=random.randint(0,len(lengthwords))     
    return lengthwords[x]
    
def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, 
    using the information in the parameters.
    '''
    guess = ""
    for l in sorted(lettersGuessed):
        guess += " "+l
        
    
    one="letters you've guessed: " + guess
    two="misses remaining = " + str(missesLeft)
    three=" ".join(hangmanWord)
    return one+"\n"+two+"\n"+three
    
def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed 
    and checks if it is a repeated letter.
    '''
    
    print(displayString)
    letter=input("letter> ")
    
    while letter in lettersGuessed:
        print("you already guessed that")
        letter=input("letter> ")
        
    return letter
    
def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord 
    and where in secretWord guessedLetter is in.
    '''
    splitsecret=[char for char in secretWord]
  
    for i in range(len(splitsecret)):
        if splitsecret[i]==guessedLetter:
            hangmanWord[i]=guessedLetter
    
   
    return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    ret=[]
    zero= updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    one= int(missesLeft)
    
    
    if guessedLetter not in secretWord:
        two= False
        one-=1
    else:
        two= True
        
    
    
    ret.append(zero)
    ret.append(one)
    ret.append(two)
    return ret

def runGame(filename):
    '''
    This function sets up the game, runs each round, 
    and prints a final message on whether or not the user won.
    True is returned if the user won the game. 
    If the user lost the game, False is returned.
    '''
    import random
   
    f = open(filename)
    words = []
    for line in f:
        words.append(line.strip())
    f.close()
    
    
    missesLeft=handleUserInputDifficulty()
    missesallowed=missesLeft
    secretWord=getWord(words,random.randint(5,10))
    
    hangmanWord=[char for char in secretWord]
    for i in range(len(hangmanWord)):
        hangmanWord[i]="_"
    
    lettersGuessed=[] 
    displayString=createDisplayString(lettersGuessed, missesLeft, hangmanWord)
     
    
    while missesLeft!=0 or secretWord!=" ".join(hangmanWord):
        
        guessedLetter=handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(guessedLetter)
        process=processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)

        
        if process[2]==True: #guessed correctly
            updateHangmanWord(guessedLetter, secretWord, hangmanWord)
            displayString=createDisplayString(lettersGuessed, missesLeft, hangmanWord)
            
            
        if process[2]==False: #guessed incorrectly
            missesLeft-= 1
            print("you missed:"+" "+guessedLetter+" not in word")
            displayString=createDisplayString(lettersGuessed, missesLeft, hangmanWord)

        if "_" not in hangmanWord: #user won
            
            print("you guessed the word: "+secretWord)
            print("you made "+str(len(lettersGuessed))+" guesses with "+str(missesallowed-missesLeft)+" misses")
            return True
    
        if missesLeft==0:
            
            print("you're hung!!")
            print("word is "+secretWord)
            print("you made "+str(len(lettersGuessed))+" guesses with "+str(missesallowed-missesLeft)+" misses")
            return False
    
if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    gameswon=0
    gameslost=0
    
    playagain='y'
    while playagain=='y':
        
        if runGame('lowerwords.txt')==True:
            gameswon+=1
        else:
            gameslost+=1
        playagain=input("Do you want to play again? y or n> ")
    
    print("You won "+str(gameswon)+" game(s) and lost "+str(gameslost))
        
        
        
    
 