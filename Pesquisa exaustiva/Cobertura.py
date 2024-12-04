def acabou(arestas, lista):
    
    for duplo in arestas:
        flag = False
        for i in lista:
            if i in duplo:
                flag = True
        if flag == False:
            return flag
    return True



def cobertura(arestas):
    nos = set()
    min = 0
    for dup in arestas:
        um = dup[0]
        dois = dup[1]
        if um not in nos:
            nos.add(um)
        if dois not in nos:
            nos.add(dois)
    min = len(nos)
    lista = []
    
    
    
    min = len(lista)
            
    return min







def main():
    print("<h3>cobertura</h3>")
    arestas = [('portugal','espanha'),('espanha','franca'),('franca','alemanha'),('alemanha','belgica'),('belgica','franca'),('usa','canada'),('usa','mexico'),('marrocos','argelia'),('argelia','libia'),('argelia','mali')]
    print("in:",arestas)
    print("out:",cobertura(arestas))

    
if __name__ == '__main__':
    main()