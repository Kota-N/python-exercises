# An exercise from http://www.practicepython.org/

#2 Odd Or Even

number = int(input('Pick a number: '))

if number % 4 == 0:
    print(str(number) + ' -> Wow, your number is a multiple of 4!')
elif number % 2 == 0:
    print(str(number) + ' -> You did it! You pick an even number!')
else:
    print(str(number) + ' -> On no, your number is odd...')