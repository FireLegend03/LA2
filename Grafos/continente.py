def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        if v in adj:
            for d in adj[v]:
                if d not in vis:
                    vis.add(d)
                    pai[d] = v
                    queue.append(d)
    return vis

def cria_dic(vizinhos):
    dic = {}
    
    for vizinho in vizinhos:
        k = vizinho[0]
        fronteiras = []
        
        for pais in vizinho[1:]:
            fronteiras.append(pais)
        if k not in dic.keys():
            dic.update({k : fronteiras})
    return dic



def maior(vizinhos):
    
    dic = cria_dic(vizinhos)
    
    grande = 0
    for k in dic:
        pai = bfs(dic,k)
        if len(pai) > grande:
            grande = len(pai)
    
    return grande



print("<h3>maior</h3>")
vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
print("in:", vizinhos)
print("out:", maior(vizinhos))