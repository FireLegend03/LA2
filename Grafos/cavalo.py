#Passou 100% dos testes
def faz_jogadas(jogadas, pos_atual):
    jogadas[pos_atual] = [(pos_atual[0] - 1, pos_atual[1] + 2), (pos_atual[0] + 1, pos_atual[1] + 2), (pos_atual[0] - 2, pos_atual[1] + 1), (pos_atual[0] - 2, pos_atual[1] - 1), (pos_atual[0] - 1, pos_atual[1] - 2), (pos_atual[0] + 1, pos_atual[1] - 2) ,(pos_atual[0] + 2, pos_atual[1] + 1) ,(pos_atual[0] + 2, pos_atual[1] - 1)]
    return jogadas


def bfs(jogadas,pos_atual,pos_final):
    pai = {}
    vis = {pos_atual}
    queue = [pos_atual]
    new_jogadas = jogadas
    while queue:
        v = queue.pop(0)
        new_jogadas = faz_jogadas(new_jogadas,v)
        for d in jogadas[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
                if d == pos_final:
                    return pai


def saltos(o,d):
    r = 0
    pos_atual = o
    pos_final = d
    if pos_atual == pos_final:
        return r
    jogadas = {}
    jogadas = faz_jogadas(jogadas, pos_atual)
    pai = bfs(jogadas,pos_atual,pos_final)
    while pos_final != o:
        r += 1
        pos_final = pai[pos_final]
    
    return r
