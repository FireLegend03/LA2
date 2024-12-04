'''

Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.

'''
#100%

from itertools import permutations

def valido(numero,d):
    num = int(numero)
    num = num % d
    if num == 0:
        return True
    else:
        return False


def multiplos(n,d):
    r = 0
    m = []
    for i in range(1,n+1):
        m.append(i)
    for i in permutations(m):
        numero = ""
        for num in i:
            numero = numero + str(num)
        if valido(numero,d):
            r += 1
    return r


def main():
    print("<h3>multiplos</h3>")
    print("in:",3,3)
    print("out:",multiplos(3,3))

    
if __name__ == '__main__':
    main()