"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.



def aux_crescente(n,lista):
    if len(lista) == 0:
        return 0
    if n < lista[0]:
        if len(lista) >= 2:
            r = 1 + aux_crescente(lista[0], lista[1:])
        else:
            r = 1
    else:
        r = aux_crescente(n, lista[1:])
    return r


def crescente(lista):
    l = len(lista)
    n = 1
    r = 0
    for numero in lista:
        if l - 2 >= n:
            m = aux_crescente(numero,lista[n:]) + 1
        elif l - 1 == n:
            m = 1
        else:
            m = 0
        n += 1
        if m > r:
            r = m
    return r
"""
#100%
def crescente(lista):
    l = len(lista)
    if l == 0:
        return 0
    if l == 1:
        return 1
    else:
        memo = {}
        memo[l - 1] = 1
        for i in range(l - 2, -1, -1):
            n = 1
            memo[i] = 1
            while i + n < l:
                if lista[i] <= lista[i + n]:
                    if memo[i] < memo[i + n] + 1:
                        memo[i] = memo[i + n] + 1
                n += 1
    return max(memo.values())



def main():
    print("<h3>crescente</h3>")
    lista = [5,2,7,4,3,8]
    print("in:",lista)
    print("out:",crescente(lista))
    
    
if __name__ == '__main__':
    main()
