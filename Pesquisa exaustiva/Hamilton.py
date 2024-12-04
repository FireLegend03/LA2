def prox(dic, lista, n, final):
    for i in dic[n]:
        if i == lista[0]:
            final[lista[0]].append(lista)
            return final
    flag = True
    for i in dic[n]:
        if i not in lista:
            flag = False
    if flag:
        return False
    for i in dic[n]:
        if i not in lista:
            lista.append(i)
            prox(dic,lista,i,final)
            lista.pop()
    return final
    

def hamilton(arestas):
    dic = {}
    for duplo in arestas:
        x = duplo[0]
        y = duplo[1]
        if x not in dic:
            dic[x] = []
        if y not in dic[x]:
            dic[x].append(y)
        if y not in dic:
            dic[y] = []
        if x not in dic[y]:
            dic[y].append(x)
    lista_final = []
    final = {}
    for inicio in dic:
        lista = [inicio]
        final[inicio] = []
        prox(dic, lista, inicio, final)
        
    if len(dic.values()) == 0:
        return None
    else:
        r_len = len(dic.keys())
        r = []
        for n in final:
            for l in final[n]:
                if len(l) > 2 and len(l) <= r_len:
                    r = l
                    r_len = len(l)
    return r
        
                


def main():
    print("<h3>hamilton</h3>")
    arestas = [(1,3),(1,4),(2,4),(3,4),(0,1),(1,2),(0,3)]
    print("in:",arestas)
    print("out:",hamilton(arestas))

    
if __name__ == '__main__':
    main()