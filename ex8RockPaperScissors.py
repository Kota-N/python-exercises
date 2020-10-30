# An exercise from http://www.practicepython.org/

#8 Rock Paper Scissors

p1 = input("P1 -> Pick paper, rock, or scissors: ")
p2 = input("P2 -> Pick paper, rock, or scissors: ")

def compare(p_1, p_2):
    if p_1 == p_2:
        if p_1 == 'rock' or p_1 == 'paper' or p_1 == 'scissors':
            print('Tie!')

    elif p_1 == 'paper':
        if p_2 == 'rock':
            print('P1 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)
        else:
            print('P2 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)

    elif p_1 == 'rock':
        if p_2 == 'paper':
            print('P2 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)
        else:
            print('P1 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)
    
    elif p_1 == 'scissors':
        if p_2 == 'paper':
            print('P1 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)
        else:
            print('P2 Wins! <- ', 'P1: ' + p_1, 'P2: ' + p_2)
    
    else:
        print('Wow, I think you typed: ' + p_1 + ' and ' + p_2)

compare(p1, p2)