#100% dos casos
def prox_move(v, mapa,tamanho_x,tamanho_y):
    jogada = set()
    x = v[0]
    y = v[1]
    if x - 1 >= 0:
        if mapa[y][x - 1] == ".":
            jogada.add((x - 1, y))
    if x + 1 < tamanho_x:
        if mapa[y][x + 1] == ".":
            jogada.add((x + 1, y))
    if y - 1 >= 0:
        if mapa[y - 1][x] == ".":
            jogada.add((x, y - 1))
    if y + 1 < tamanho_y:
        if mapa[y + 1][x] == ".":
            jogada.add((x, y + 1))
    return jogada


def bfs(mapa,o):
    r = 1
    tamanho_x = len(mapa[0])
    tamanho_y = len(mapa)
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        jogada = prox_move(v,mapa,tamanho_x,tamanho_y)
        for d in jogada:
            if d not in vis:
                vis.add(d)
                queue.append(d)
                r += 1
    return r


def area(p,mapa):
    if mapa[p[1]][p[0]] == "*":
        return 0
    r = bfs(mapa, p)
    return r


print("<h3>area</h3>")
mapa = ["..*..",
        ".*.*.",
        "*...*",
        ".*.*.",
        "..*.."]
print("in:",(3,2))
print('\n'.join(mapa))
print("out:",area((3,2),mapa))