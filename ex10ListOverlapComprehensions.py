# An exercise from http://www.practicepython.org/

#10 List Overlap Comprehensions

import random

list1 = random.sample(range(30), 17)
list2 = random.sample(range(30), 15)

answer_list = [x for x in list1 if x in list2]


answer_list.sort()
print(answer_list)