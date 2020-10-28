# Exercises from http://www.practicepython.org/

#5 List Overlap

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

answer_list = []

for i in list1:
    if i in list2:
        if not i in answer_list:
            answer_list.append(i)

print(answer_list)