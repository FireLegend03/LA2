"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente._

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""

#60% dos casos, não usa prog dinâmica

def vendedor(capacidade,produtos):
    r = aux_vendedor(capacidade, produtos,{})
    l = sorted(r[1])
    n = (r[0], l)
    return n

def aux_vendedor(capacidade,produtos,memo):
    r = (0, [])
    if capacidade in memo:
        return memo[capacidade]
    elif capacidade == 0:
        memo[0] = r
        return memo[0] 
    else:
        for produto in produtos:
            if produto[2] <= capacidade:
                n = vendedor(capacidade - produto[2], produtos)
                lucro = n[0] + produto[1]
                lista = n[1]
                lista.insert(0, produto[0])
                if lucro > r[0]:
                    temp_n = (lucro, lista)
                    r = temp_n     
    memo[capacidade] = r
    return memo[capacidade]


def main():
    print("<h3>vendedor</h3>")
    produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    print("in:",14,produtos)
    print("out:",vendedor(14,produtos))

if __name__ == '__main__':
    main()