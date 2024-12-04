"""

Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

"""

def saque_aux(mapa,x,y,memo):
    r = 0
    if (x,y) in memo:
        return memo[(x,y)]
    if mapa[y][x] == '#':
        memo[(x,y)] = -1000
        return -1000
    if x == len(mapa[0]) - 1 and y == len(mapa):
        return 0
    else:
        if x + 1 < len(mapa[0]):
            n = saque_aux(mapa, x + 1, y, memo)
            if r < n:
                r = n
        if y + 1 < len(mapa):
            m = saque_aux(mapa,x,y + 1, memo)
            if r < m:
                r = m
        if mapa[y][x] != ".":
            r += int(mapa[y][x])
    memo[(x,y)] = r
    return r

def saque(mapa):
    return saque_aux(mapa, 0, 0, {})


def main():
    print("<h3>saque</h3>")
    mapa = [".3......",
            "........",
            "...5#...",
            "...##...",
            ".....9..",
            "..2.....",
            "..2.....",
            "..2....."]
    print("in:")
    print('\n'.join(mapa))
    print("out:",saque(mapa))

    
if __name__ == '__main__':
    main()