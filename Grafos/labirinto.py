def bfs(mapa):
    o = (0,0)
    tamanho_x = len(mapa[0]) - 1
    tamanho_y = len(mapa) - 1
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        jogadas = possiveis(v,mapa,tamanho_x,tamanho_y)
        for d in jogadas[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
                if d[0] == tamanho_x and d[1] == tamanho_y:
                    return pai


def possiveis(v,mapa,tamanho_x,tamanho_y):
    jogadas = {}
    lista = []
    if v[0] + 1 <= tamanho_x:
        if mapa[v[1]][v[0] + 1] == " ":
            lista.append((v[0] + 1,v[1], "E"))
    if v[0] > 0:
        if mapa[v[1]][v[0] - 1] == " ":
            lista.append((v[0] - 1,v[1], "O"))
    if v[1] + 1 <= tamanho_y:
        if mapa[v[1] + 1][v[0]] == " ":
            lista.append((v[0],v[1] + 1, "S"))
    if v[1] > 0:    
        if mapa[v[1] - 1][v[0]] == " ":
            lista.append((v[0],v[1] - 1, "N"))
    jogadas[v] = lista
    return jogadas

def caminho(mapa):
    pai = bfs(mapa)
    r = list(pai.keys())[-1]
    r1 = (r[0],r[1])
    caminho = ""
    while r1 != (0,0):
        caminho += r[2]
        r = pai[r]
        r1 = (r[0],r[1])
    caminho = caminho[::-1]
    return caminho

print("<h3>caminho</h3>")
mapa = mapa = ['   ',
                ' # ',
                '   ']
print("in:")
print('\n'.join(mapa))
print("out:",caminho(mapa))