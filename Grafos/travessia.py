#80% dos casos
import math
def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

def faz_triplos(mapa):
    tamanho_x = len(mapa[0])
    tamanho_y = len(mapa)
    lista = []
    peso = 0
    iy = 0
    ix = 0
    while iy < tamanho_y:
        while ix < tamanho_x:
            if ix + 1 < tamanho_x and abs(int(mapa[iy][ix]) - int(mapa[iy][ix + 1])) <= 2:
                peso = abs(int(mapa[iy][ix]) - int(mapa[iy][ix + 1])) + 1
                lista.append(((ix, iy), (ix + 1, iy), peso))
            if iy + 1 < tamanho_y and abs(int(mapa[iy][ix]) - int(mapa[iy + 1][ix])) <= 2:
                peso = abs(int(mapa[iy][ix]) - int(mapa[iy + 1][ix])) + 1
                lista.append(((ix, iy), (ix, iy + 1), peso))
            ix += 1
        iy += 1
        ix = 0
    return lista

def faz_dic(lista):
    dic = {}
    for o,d,p in lista:
        if o not in dic:
            dic[o] = {}
        if d not in dic:
            dic[d] = {}
        dic[o][d] = p
        dic[d][o] = p
    return dic


def travessia(mapa):
    if mapa == []:
        return (0,0)
    lista = faz_triplos(mapa)
    dic = faz_dic(lista)
    lista = fw(dic)
    tamanho_x = len(mapa[0])
    tamanho_y = len(mapa)
    peso = float("inf")
    cord = tamanho_x + 1
    x1 = 0
    x2 = 0
    y = tamanho_y - 1
    while x1 < tamanho_x:
        while x2 < tamanho_x:
            if (x1,0) in lista and (x2,y) in lista:
                if lista[(x1,0)][(x2,y)] < peso:
                    peso = lista[(x1,0)][(x2,y)]
                    cord = x1
                elif lista[(x1,0)][(x2,y)] == peso:
                    if x1 < cord:
                        peso = lista[(x1,0)][(x2,y)]
                        cord = x1
            x2 += 1
        x1 += 1
        x2 = 0
    if math.isinf(peso):
        return (0,0)
    return (cord,peso)

print("<h3>travessia</h3>")
mapa = ["90999",
        "00000",
        "92909",
        "94909"]
print("in:")
print('\n'.join(mapa))
print("out:",travessia(mapa))