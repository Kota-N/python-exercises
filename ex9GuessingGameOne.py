# An exercise from http://www.practicepython.org/

#9 Guessing Game One

from random import randint

def guessing_game():
    answer = randint(1, 9)
    guess_count = 0
    print('(Type "exit" to exit)')
    pick_a_number(answer, guess_count)

    

def pick_a_number(answer, guess_count):
    user_guess = input("Please pick a number from 1 to 9: ")
    

    if user_guess == 'exit':
        quit()
    elif int(user_guess) > 9 or int(user_guess) < 1:
        print('Your number needs to be a number from 1 to 9.')
        pick_a_number(answer, guess_count)
    elif int(user_guess) == answer:
        print('Congrats!\nAnswer: ' + str(answer) + ', your number: ' + user_guess + ', you guessed ' + str(guess_count + 1) + ' times!')
        return
    elif int(user_guess) > answer:
        print('Too high!')
        pick_a_number(answer, guess_count + 1)
    elif int(user_guess) < answer:
        print('Too low!')
        pick_a_number(answer, guess_count + 1)

guessing_game()