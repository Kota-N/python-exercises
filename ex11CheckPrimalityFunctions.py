# An exercise from http://www.practicepython.org/

#4 Check Prime Functions


def get_int():
    num = int(input('Pick a number: '))
    return num

def get_divisors(num):
    num_list = range(2, num -1)
    divisors_list = []

    for x in num_list:
        if num % x == 0:
            divisors_list.append(x)
    
    return divisors_list

def is_prime(num):
    if len(get_divisors(num)) == 0:
        print(str(num) + ' is a prime number!')
    else:
        print(str(num) + ' can be divided by these numbers: ' + str(get_divisors(num)))


num = get_int()
is_prime(num)