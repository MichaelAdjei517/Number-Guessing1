from colors import *
from random import randint
#welcome to the wold of Gaming
print(BLUE,'***Welcome to the world of Guessing ***')
User_input = int(input(WHITE +'Chose your level\n'
                           '1. Normal (1 -50)\n'
                            '2. Intermeditae (1 - 500)\n'
                           '3. Hard (1-500)\n'
                           '4. Exit Apllication\n\n  '
                              'Enter request:  '))
#user's option
guess_range = 0
if User_input ==1:
    guess_range = 50
elif User_input == 2:
    guess_range =200
elif User_input == 3:
    guess_range =500
elif User_input == 4:
  print('*** Thanks for Using Our App, Hope to hear from you again')
  exit(1)
else:
    print = (RED, "Invalid Request, Try Again")

# Generating random number between eartain range
generate_number = randint(1,guess_range)

#user chances
user_chances = 4
for i in range(4):
    user_guess = input('Provide Your Guess Number : ')
    if user_guess == generate_number:
     print(GREEN,f'Hurray!!!, You Guess It Correct')
     break
    elif user_guess > generate_number:
     print(YELLOW, 'Your Guess Too High,Try Again.')
     user_chances-= 1
     print (f'number of chances Left is {user_chances}')

