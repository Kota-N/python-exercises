# An exercise from http://www.practicepython.org/

#7 List Comprehensions

num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_num = [x for x in num_list if x % 2 == 0]

print(even_num)