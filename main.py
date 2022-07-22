"""
This is a simple number guessing game made with python. The rules are simple:

    i. Guess a number in between 1 to 30;
    ii. The guessed number will be compared with the randomly generated number;
    iii. If both matches , the user wins and loose otherwise.

One twist in the game is that one can't guess more than 3 times in a row.

"""


# generating random number
import random
random_number = random.randint(1,30)

# set flag value 
count = 0

while (count != 3):
  print('Enter your guess between 1-30: \t')
  user_input = int(input());

# checking input range
  if (user_input > 0 and user_input <= 30):
    count += 1

    if (user_input == random_number):
      print ('You won!')
      break;

    else:
      print('You loose!')
      attempt = 3 - count
      print(attempt, 'attemps left...')

  else:
    print('Oops! Enter your guess between 1-30: \t')

print('The randomly generated number was: ', random_number)

