import random

# Ask user to select the range ->  lower bound to upper bound
value1,value2 = map(int, input("Enter the range (lower upper): ").split())

if value1>value2:
    value1,value2 = value2,value1

#program select random number
num_to_guess = random.randrange(value1,value2)

#Constant value
GUESS = 7

while GUESS>0:
    print("Guess remaining: ",GUESS)
    user_guess = int(input('Enter the guess value'))
    if user_guess > num_to_guess:
        print('Your guess is higher')
    elif user_guess< num_to_guess:
        print('Your guess is lower')
    elif user_guess == num_to_guess:
        print('you hit bulleye!!!')
        break
    else:
        print('Fucking Dumb!!!')
    GUESS -=1
print('game over....')


