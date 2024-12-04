"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
#10%
def espaca(frase, palavras):
    l = frase
    tamanho = len(frase) - 1
    if frase == "":
        return ""
    else:
        cont = 1    
        palavra = ""
        for letra in range(tamanho, -1, -1):
            palavra = frase[letra] + palavra
            if palavra in palavras:
                n = " " + palavra
                r = (espaca(frase[:-cont], palavras)) + n
                if len(r) > len(l):
                    l = r
            cont += 1
    return l


def main():
    print("<h3>espaca</h3>")
    palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
    print("in:","estecursoeomaior",palavras)
    print("out:",espaca("estecursoeomaior",palavras))
    
    
if __name__ == '__main__':
    main()
