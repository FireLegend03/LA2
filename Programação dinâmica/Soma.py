"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

def maxsoma(lista):
    if lista == []:
        return 0
    if len(lista) == 1:
        return lista[0]
    else:
        memo = {}
        l = len(lista)
        memo[l - 1] = lista[l - 1]
        for i in range(l - 2, -1, -1):
            n = 1
            memo[i] = lista[i]
            r = memo[i]
            m = l - 1
            while i < l - n:
                soma = sum(lista[i:l - n])
                if soma >= r:
                    r = soma
                n += 1
            if r >= memo[i]:
                    memo[i] = r
    return max(memo.values())
"""
#100% (não é meu)
def maxsoma(lista):
    l = len(lista)
    if l == 0:
        return 0
    maximo = lista[0]
    r = []
    r.append(maximo)
    for i in range(1, l):
        r.append(max(r[i - 1] + lista[i], lista[i]))
        maximo = max(r[i], maximo)
    return maximo



def main():
    print("<h3>maxsoma</h3>")
    lista = [-2,1,-3,4,-1,2,1,-5,4]
    print("in:",lista)
    print("out:",maxsoma(lista))

    
if __name__ == '__main__':
    main()