# 100% dos casos
def rotas_na_bomba(rotas):
    i = 0
    rotas_fim = []
    while i < len(rotas):
        r = 2
        while r < len(rotas[i]):
            rotas_fim.append((rotas[i][r], rotas[i][r - 2], rotas[i][r - 1]))
            r += 2
        i += 1
    return rotas_fim


def faz_dict_v2(rotas_fim):
    adj = {}
    for origem, dest, peso in rotas_fim:
        if origem not in adj:
            adj[origem] = {}
        if dest not in adj:
            adj[dest] = {}
        adj[origem][dest] = peso
        adj[dest][origem] = peso
        
    return adj


def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist


def viagem(rotas,o,d):
    if o == d:
        return 0
    rotas_fim = rotas_na_bomba(rotas)
    adj = faz_dict_v2(rotas_fim)
    price = dijkstra(adj,o)
    return price[d]