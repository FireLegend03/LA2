'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

'''

def sacos(peso,compras):
    final = sum(compras)
    r = 0
    if (final % peso) == 0:
        r = final / peso
    else:
        while final > 0:
            final -= peso
            r+=1
        
    return r


def main():
    print("<h3>sacos</h3>")
    compras = [3,6,2,1,5,7,2,4,1]
    print("in:",10,compras)
    print("out:",sacos(10,compras))

    
if __name__ == '__main__':
    main()