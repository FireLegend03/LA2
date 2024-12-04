'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.

'''
#90%

def valido(dic, lista, i):
    for pessoa in lista:
        if i not in dic[pessoa]:
            return False
    return True


def prox(dic, pessoa, lista):
    flag = 0
    for i in dic[pessoa]:
        if valido(dic, lista, i):
            flag = 1
    if flag == 0:
        return True
    for i in dic[pessoa]:
        if valido(dic, lista, i):
            lista.append(i)
            if prox(dic, pessoa, lista):
                return True
            lista.pop()
    return False
            
        


def amigos(conhecidos):
    dic = {}
    for duplo in conhecidos:
        if duplo[0] not in dic:
            dic[duplo[0]] = []
        if duplo[1] not in dic[duplo[0]]:
            dic[duplo[0]].append(duplo[1])
        
        if duplo[1] not in dic:
            dic[duplo[1]] = []
        if duplo[0] not in dic[duplo[1]]:
            dic[duplo[1]].append(duplo[0])
            
    max = 1
    for pessoa in dic:
        lista = [pessoa]
        if prox(dic, pessoa, lista):
            c = len(lista)
            if c > max:
                max = c
    
    return max


def main():
    print("<h3>amigos</h3>")
    conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
    print("in:",conhecidos)
    print("out:",amigos(conhecidos))

    
if __name__ == '__main__':
    main()
