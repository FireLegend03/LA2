'''

Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.

'''
#60%

def valido(lista, set):
    for i in lista:
        if i == set:
            return False
    return True
    


def prox(sets, numeros, lista):
    tamanho_lista = 0
    for set in lista:
        tamanho_lista += len(set)
    if tamanho_lista == len(numeros):
        return True
    
    for set in sets:
        if valido(lista, set):
            lista.append(set)
            if prox(sets, numeros, lista):
                return True
            lista.pop()
    return False
            
        
        
    return False

def uniao(sets):
    if len(sets) == 0:
        return 0
    numeros = []
    for i in sets:
        for d in i:
            if d not in numeros:
                numeros.append(d)
    n = len(sets)
    
    for set in sets:
        lista = []
        lista.append(set)
        if prox(sets, numeros, lista):
            c = len(lista)
            if c < n:
                n = c
        
    return n



def main():
    print("<h3>uniao</h3>")
    sets = [{1,2,3},{2,4},{3,4},{4,5}]
    print("in:",sets)
    print("out:",uniao(sets))

    
if __name__ == '__main__':
    main()
