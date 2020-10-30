# An exercise from http://www.practicepython.org/

#4 Divisors

num = int(input('Pick a number: '))

num_list = range(2, num -1)

for x in num_list:
    if num % x == 0:
        print(x)