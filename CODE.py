import random
#importing the random library for choosing random words


hanger=['''
                +-----+
                |     |
                      |
                      |
                      |
                     _|_
                   |-----|''', '''
                +-----+
                |     |
                0     |
                      |
                      |
                     _|_''', '''
                +-----+
                |     |
                0     |
                |     |
                |     |
                     _|_''', '''
                +-----+
                |     |
                0     |
               /|     |
                |     |
                     _|_''', '''
                +-----+
                |     |
                0     |
               /|\    |
                |     |
                     _|_''', ''' 
                +-----+
                |     |
                0     |
               /|\    |
                |     |
               /     _|_''', '''
                +-----+
                |     |
                0     |
               /|\    |
                |     |
               / \   _|_
          
__-*-__-*-__-*-_MAN DIED_-*-__-*-__-*-__ ''' ,'''
__-*-____-*-____-*-____-*-____-*-____-*-____-*-__         
                    \o/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 
              CHIKEN DINNER                           

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
#graphics


def get():
  print("DO YOU WANT TO PLAY MORE")
  choice=input("ENTER YES OR NO\n")
  choice=choice.upper()
  if(choice=="YES"):
     return True;
  elif(choice=="NO"): 
     print("********---THANK YOU---*********")
     print("#######xxxxxxxxxxxxxxxxxx#########")
     return False
  else:
    print("Wrong input, PLZ enter yes/YES/no/NO only")
    get()
# A function to know if the user want to play more or not


wantToPlay=True
# initialising a boolean wantToPlay to True
while wantToPlay==True: 
  word_list="dog cat donkey whale fox tiger lion giraffe goat gorilla hippopotamuse bat bear elephant pig rabbit wolf crow owl penguin crab jellyfish snail ".split()
  # string of words separeted by split function

  turns=6
  #initialising the turns to 6
  wrong=0  
  right=[]
  #initiating integer wrong and list right
  guessed_letters=[]
  # a list to store guessed letters


  def get_word():
    w=random.choice(word_list)
    return w
  #function to choose word from word_list

  word=get_word()
  #calling get_word() function

  word=word.upper()
  #making the lower case word into upper case

  blanks=[]
  for i in range(0,len(word)):
     blanks.append("-")
  # list of '-' blanks


  print("*****WELCOME TO HANGMAN GAME!!!*****")
  name=input("WHAT IS YOUR NAME?? \n")
  print("Good Luck ! ", name)
  print("## SAVE THE MAN ##")
  #getting the name of the user and welcoming the user


  print(hanger[0])
  print("YOU HAVE ONLY 6 TURNS TO SAVE THE MAN")
  #printing the first animation and information about the turns

  b=""
  b=b.join(blanks)
  print(" "+b+" ")
  # converting list blanks to string b


  f=False  

  while f==False:
    right=[]
    
    guess=input("Guess a letter -> ")
    print()
    print("_"*50)
    print("_+_-*-_+_"*7)
    print()
    print()
    guess=guess.upper()
    if len(guess) != 1:
      print("Pick One Letter At A Time")
      continue
    elif guess in guessed_letters:
      print(" " + guess + " Has Already Been Chosen, Try Again")
      continue
    elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      print("Only Pick Letters")
      continue
    else:
      guessed_letters.append(guess)
    # getting the guess                
  

    if not guess in word:
      wrong=wrong+1
      turns=turns-1
    # getting the guessed letter from the user


    for i in range(len(word)):
     if word[i] in guessed_letters:
       b=b[:i] + word[i] + b[i+1:]                
       right.append(i)
       # appending to the right list if the guessed word is present in the word


    print(" " + b + " ") 
    print("guessed letters are: ", end=" ")
    for i in range(len(guessed_letters)):
      print(guessed_letters[i],",",end=' ')   
    # giving information about how many blanks are remaining
    # and how many words are already guessed


    if wrong < 6:
      print(hanger[wrong])
      print("YOU HAVE ONLY ",turns, "TURN TO SAVE A LIFE")
    # information about how many turns are left to play


    if wrong == 6:
      print(hanger[wrong])
      print()
      print("***********YOU LOOSE***********")
      print("The word was:")
      print(">>>>>>>>>>>>>>",word,"<<<<<<<<<<<<<<<")
      # when player out of turns a message you loose is printed 
      f=True
      wantToPlay=get()
      # getting coice
      # user want to play more or not
        

    if len(right)==len(word):
      print(hanger[7])
      print("**********you won**********")
      print("*******you saved a life*******")
    # when player guesss the whole word correctly 
    # a message you won is printed             
      f=True
      wantToPlay=get()
      # getting choice
      # user wnt to play more or not
          

# A while loop for the execution of the program 
# program ended         