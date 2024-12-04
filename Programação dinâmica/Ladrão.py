"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""

def ladrao_aux(capacidade,objectos, memo):
    r = 0
    if capacidade in memo:
        return memo[capacidade]
    if capacidade == 0:
        memo[0] = 0
        return 0
    for objeto in objectos:
        if objeto[2] <= capacidade:
            n = objeto[1] + ladrao_aux(capacidade - objeto[2], objectos[1:], memo)
            if n > r:
                r = n
    memo[capacidade] = r
    return r

def ladrao(capacidade, objetos):
    return ladrao_aux(capacidade, objetos, {})