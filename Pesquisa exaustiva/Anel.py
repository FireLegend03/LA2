from itertools import permutations

def primo(r):
    for n in range(2,r,1):
        if r%n == 0:
            return False
    return True

def valido(i):
    if primo(i[0] + i[-1]) == False:
        return False
    for n in range(len(i) - 1):
        if primo(i[n] + i[n + 1]) == False:
            return False
    return True


def anel(n):
    
    for i in permutations(range(1,n + 1)):
        if(valido(i)):
            return list(i)
    return []