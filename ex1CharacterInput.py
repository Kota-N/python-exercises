# An exercise from http://www.practicepython.org/

#1 Character Input

name = input('What is your name?: ')
age = int(input('How old are you?: '))

if age < 100:
    print('Hi ' + name + '! You will be 100 years old in ' + str(100 - age) + ' years.')
else:
    print('Oh no, you have already reached 100 years old!')


