'''

Implemente um função que calcula a menor string que contém todas as palavras 
recebidas na lista de input. Assuma que todas as palavras são disjuntas entre si, 
ou seja, nunca haverá inputs onde uma das palavras está contida noutra.

40%
'''
from itertools import permutations
def superstring(strings):
    lista = []
    for palavra in strings:
        for letra in palavra:
            if letra not in lista:
                lista.append(letra)
    for i in permutations(lista):
        palavra = ""
        r = 0
        for letra in i:
            palavra = palavra + letra
        for string in strings:
            if string in palavra:
                r += 1
        if r == len(strings):
            return palavra
        
    return ""

def main():
    print("<h3>superstring</h3>")
    strings = ['an','na','m']
    print("in:",strings)
    print("out:",superstring(strings))

    
if __name__ == '__main__':
    main()
