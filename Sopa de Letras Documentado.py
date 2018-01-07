"""TIPO DIRECAO"""

"""e_direcao: universal --> boolean
e_direcao(arg) verifica se o argumento pertence ao tipo direcao. E verdadeiro se tal acontecer e falso caso contrario."""
def e_direcao(arg):
    return arg in ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']

"""e_norte: direcao--> boolean
e_norte(arg) verifica se o argumento e o elemento 'N'."""
def e_norte(arg):
    return arg == 'N'

"""e_sul: direcao--> boolean
e_sul(arg: verifica se o argumento e o elemento 'S'."""
def e_sul(arg):
    return arg == 'S'

"""e_leste: direcao--> boolean
e_leste(arg) verifica se o argumento e o elemento 'E'."""
def e_leste(arg):
    return arg == 'E'

"""e_oeste: direcao--> boolean
e_oeste(arg) verifica se o argumento e o elemento 'W'."""
def e_oeste(arg):
    return arg == 'W'

"""e_nordeste: direcao--> boolean
e_nordeste(arg) verifica se o argumento e o elemento 'NE'."""
def e_nordeste(arg):
    return arg == 'NE'

"""e_noroeste: direcao--> boolean
e_noroeste(arg)verifica se o argumento e o elemento 'NW'."""
def e_noreste(arg):
    return arg == 'NW'

"""e_sudeste: direcao--> boolean
e_sudeste(arg) verifica se o argumento e o elemento 'SE'."""
def e_sudeste(arg):
    return arg == 'SE'

"""e_sudoeste: direcao--> boolean
e_sudoeste(arg) verifica se o argumento e o elemento 'SW'."""
def e_sudoeste(arg):
    return arg == 'SW'

"""direcoes_iguais: direcao x direcao --> boolean
direccoes_iguais (dir1, dir2) devolve o valor verdadeiro apenas se as direcoes dir1 e dir 2 forem iguais."""
def direcoes_iguais(dir1, dir2):
    return dir1 == dir2

"""direcao_oposta: direcao --> direcao
direcao_oposta (drc) devolve a direcao oposta de drc de acordo com a ros dos ventos."""
def direcao_oposta(drc):
    rosa_ventos = {'N':'S', 'S':'N', 'W':'E', 'E':'W', 'NW':'SE', 'SE':'NW', 'NE': 'SW', 'SW':'NE'}
    return rosa_ventos[drc]


"""TIPO COORDENADA"""

"""coordenada : int x int x direcao --> coordenada
coordenada(l; c; d) tem como valor a coordenada referente a posicao (l;c) e a 
direção d. Em caso de erro, coordenada l; c; d) gera uma mensagem de erro."""
def coordenada(l,c,d):
    if not verifica_coordenada(l,c,d):
        raise ValueError('coordenada: argumentos invalidos')
    return (l,c,d)
    
"""coord_linha : coordenada --> int
coord_linha (c) tem como valor a linha da coordenada."""    
def coord_linha(c):   
    return c[0]   

"""coord_linha : coordenada --> int
coord_linha (c) tem como valor a coluna da coordenada.""" 
def coord_coluna(c):
    return c[1]

"""coord_linha : coordenada --> direccao
coord_linha (c) tem como valor a direccao da coordenada.""" 
def coord_direcao(c):
    return c[2]

"""e_coordenada : universal --> boolean
e_coordenada(arg) verifica se o argumento e do tipo coordenada. E verdadeiro se tal acontecer e falso caso contrario."""
def e_coordenada(arg):
    if isinstance(arg, tuple) and len(arg) == 3:
        return verifica_coordenada(coord_linha(arg),coord_coluna(arg),coord_direcao(arg))
    return False

"""coordenadas_iguais : coordenada x coordenada --> boolean
coordenadas_iguais(c1, c2) verifica se duas coordenadas sao iguais. E verdadeiro se tal acontecer e falso caso contrario."""
def coordenadas_iguais(c1,c2):
    return c1 == c2

"""coordenada_string : coordenada --> string
coordenada_string(c) devolve a representacao externa de c."""
def coordenada_string(c):
    return '(' + str(c[0]) + ', ' + str(c[1]) + ')-' + c[2]


"""TIPO GRELHA"""

"""grelha: lst --> grelha
grelha(lst) tem como valor uma grelha m*n, em que m e o numero de elementos da lista lst e n o numero de caracteres de cada string. A lista nao pode ser vazia e as strings tem de ter o mesmo comprimento. Em caso de erro, grelha(lst) gera uma mensagem de erro"""
def grelha(lst):
    if verifica_tipos_argumento(lst) and verifica_todos_string(lst) and verifica_comps_iguais(lst) and verifica_repeticoes(lst):
        return lst
    raise ValueError('grelha: argumentos invalidos')
    
"""grelha_nr_linhas: grelha --> int
grelha_nr_linhas(g) devolve o numero de linhas da grelha g."""
def grelha_nr_linhas(g):
    return len(g)

"""grelha_nr_colunas: grelha --> int
grelha_nr_linhas(g) devolve o numero de colunas da grelha g."""
def grelha_nr_colunas(g):
    return len(g[0])

"""grelha_elemento: grelha x int x int--> caracter
grelha_elemento(g, l, c) devolve o caracter situado na posicao (l, c) da grelha g. Caso a posicao (l, c) nao seja valida para a grelha g, grelha_elemento gerara uma mensagem de erro."""
def grelha_elemento(g,l,c):
    linhas = grelha_nr_linhas(g)
    colunas = grelha_nr_colunas(g)
    if l in range(0,linhas) and c in range(0, colunas):
        return g[l][c]
    raise ValueError('grelha_elemento: argumentos invalidos')

"""grelha_linha: grelha x coordenada --> string
grelha_linha (g, c) devolve a cadeia de caracteres que corresponde a linha definida segundo a direccao dada pela coordenada c, e que inclui a posicao dada pela mesma coordenada. Caso c nao defina uma posicao valida para a grelha g, grelha_linha gerara uma mensagem de erro."""
def grelha_linha(g,c):
    linhas = grelha_nr_linhas(g)
    colunas = grelha_nr_colunas(g)
    linha = coord_linha(c)
    coluna = coord_coluna(c)
    direcao = coord_direcao(c)
    resposta = ''
    if linha >= linhas or coluna >= colunas:
        raise ValueError('grelha_linha: argumentos invalidos')
    else:
        if e_sul(direcao):
            for l in range(linhas):
                resposta = resposta + grelha_elemento(g, l, c[1])
        if e_norte(direcao):
            for l in range(linhas-1,-1,-1):
                resposta = resposta + grelha_elemento(g,l,c[1])
        if e_leste(direcao):
            for col in range(colunas):
                resposta = resposta + grelha_elemento(g, c[0], col)
        if e_oeste(direcao):
            for col in range(colunas-1,-1,-1):
                resposta = resposta + grelha_elemento(g,c[0],col)
        if e_nordeste(direcao):
            while linha + 1 in range(linhas) and coluna -1 in range(colunas):
                linha = linha + 1
                coluna = coluna -1
            while linha in range(linhas) and coluna in range(colunas):
                resposta = resposta + grelha_elemento(g, linha,coluna)
                linha = linha -1
                coluna = coluna + 1
        if e_noroeste(direcao):
            while linha+1 in range(linhas) and coluna+1 in range(colunas):
                linha = linha + 1
                coluna = coluna + 1
            while linha in range(linhas) and coluna in range(colunas):
                resposta = resposta + grelha_elemento(g, linha,coluna)
                linha = linha - 1
                coluna = coluna - 1
        if e_sudeste(direcao):
            while linha-1 in range(linhas) and coluna-1 in range(colunas):
                linha = linha - 1
                coluna = coluna - 1
            while linha in range(linhas) and coluna in range(colunas):
                resposta = resposta + grelha_elemento(g, linha, coluna)
                linha = linha + 1
                coluna = coluna + 1
        if e_sudoeste(direcao):
            while linha-1 in range(linhas) and coluna+1 in range(colunas):
                linha = linha - 1
                coluna = coluna + 1
            while linha in range(linhas) and coluna in range(colunas):
                resposta = resposta + grelha_elemento(g, linha,coluna)
                linha = linha + 1
                coluna = coluna - 1           
        return resposta
"""e_grelha: universal --> boolean
e_grelha(arg) verifica se o argumento e do tipo grelha. E verdadeiro se tal acontecer e falso caso contrario."""
def e_grelha(arg):
    return verifica_tipos_argumento(arg) and verifica_todos_string(arg) and verifica_comps_iguais(arg) and verifica_repeticoes(arg)
    

"""grelhas_iguais: grelha x grelha --> boolean
grelhas_iguais (g1, g2) devolve o valor verdadeiro apenas se as grelhas g1 e g2 forem iguais."""
def grelhas_iguais(g1,g2):
    return g1 == g2


"""TIPO RESPOSTA (lista composta por dois tuplos: um com uma string e um com uma coordenada)"""

"""resposta: list --> resposta
resposta (lst) tem como valor a resposta que contem cada um dos tuplos que compoe a lista lst. Em caso de erro, resposta gera uma mensagem de erro."""
def resposta(lst):
    if isinstance(lst, list) and verifica_elementos_tuplos(lst) and verifica_tuplos_corretos:
        return lst
    raise ValueError('resposta: argumentos invalidos')
    
"""resposta_elemento: resposta x int --> tuple (string, coordenada)
resposta_elemento (res, n) devolve o n-esimo elemento da resposta res. Caso n seja menor do que 0 ou maior ou igual que o numero de elementos da resposta erro, resposta_elemento gerara uma mensagem de erro."""
def resposta_elemento(res,n):
    if n < 0 or n >= len(res):
        raise ValueError('resposta_elemento: argumentos invalidos')
    return res[n]

"""resposta_tamanho: resposta --> int
resposta_tamanho(res) devolve o numero de elementos da resposta res."""
def resposta_tamanho(res):
    return len(res)

"""acrescenta_elemento: resposta x string x coordenada --> resposta
acrescenta_elemento(r, s, c) devolve a resposta n com mais um elemento: o tuplo (s, c)"""
def acrescenta_elemento(r,s,c):
    elemento = (s,c)
    if elemento in r:
        return r
    else:
        return r + [elemento]

"""e_resposta: universal --> boolean
e_resposta(arg) verifica se o argumento e do tipo resposta. E verdadeiro se tal se verificar e falso caso contrario."""
def e_resposta(arg):
    return isinstance(arg, list) and verifica_elementos_tuplos(arg) and verifica_tuplos_corretos(arg)

"""respostas_iguais: resposta x resposta --> boolean
respostas_iguais (r1, r2) devolve o valor verdadeiro apenas se as respostas r1 e r2 forem iguais."""
def respostas_iguais(r1,r2):
    Iguais = True
    for tup in r1:
        if tup not in r2:
            Iguais = False
    return Iguais

"""resposta_string: resposta --> string
resposta_string(res) devolve a representacao externa da resposta res."""
def resposta_string(res):
    string = '['
    res = ordena(res)
    for ele in res:
        string = string + '<' + ele[0]+ ':' + coordenada_string(ele[1]) + '>' + ', '
    return string[:len(string)-2] + ']'


"""FUNCOES PRINCIPAIS"""

"""sopa_letras: cadeia de caracteres --> resposta
sopa_letras(fich) tem como resultado a resposta ao puzzle descrito no ficheiro fich."""
def sopa_letras(fich):
    file = open(fich, 'r')
    lst_linhas = file.readlines()
    string = lst_linhas[1][10:len(lst_linhas[1])-1]
    palavras = string_para_lista(string) 
    letras = []
    for i in range(2, len(lst_linhas)):
        letras = letras + [lst_linhas[i][:len(lst_linhas[i])-1]]
    letras[-1] = letras[-1][:len(letras[-1])]
    return letras

"""procura_palavras_numa_direcao : grelha x list x direcao --> resposta
procura_palavras_numa_direcao(grelha; palavras; dir) tem como resultado
a resposta que representa as coordenadas das palavras encontradas na grelha.


######## FUNCOES AUXILIARES ###############

"""ordena: --> boolean
ordena(r)"""
def ordena(r):
    Troca = True
    while Troca:
        Troca = False
        for i in range(len(r) - 1):
            if r[i][0] > r[i+1][0]:
                r[i], r[i+1] = r[i+1], r[i]
                Troca = True
    return r

"""verifica_coordenada: int x int x direccao --> boolean
verifica_coordenada(l, c, d) verifica se cada um dos argumentos da coordenada e valido. E verdadeiro se todos sao validos e falso caso contrario"""
def verifica_coordenada(l,c,d):
    if isinstance(l, int) and isinstance(c,int) and e_direcao(d) and l >=0 and c >=0:
        return True
    return False

"""verifica_tipos_argumento: list --> boolean
verifica_tipos_argumento(lst) verifica os tipos dos argumentos."""        
def verifica_tipos_argumento(lst):
    if isinstance(lst, list) and isinstance(lst[0], str):
        return True
    else:
        return False
    
"""verifica_todos_string: list --> boolean
verifica_todos_string(lst) verifica se todos os argumentos da lista sao strings."""
def verifica_todos_string(lst):
    for ele in lst:
        if not isinstance(ele, str):
            return False
    return True

"""verifica_comps_iguais: list --> boolean
verifica_comps_iguais(lst) verifica se os comprimentos das strings que compoe a lista sao iguais."""
def verifica_comps_iguais(lst):
    comp = len(lst[0])
    for ele in lst:
        if len(ele) != comp:
            return False
    return True

"""verifica_repeticoes: list --> boolean
verifica_repeticoes(lst) verifica se algum elemento da lista se repete."""
def verifica_repeticoes(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            return False
    return True
    
"""verifica_elementos_tuplos: universal --> boolean
verifica_elementos_tuplos(lst) verifica se os elementos do argumento sao tuplos. E verdadeiro se tal se verificar e falso caso contrario."""
def verifica_elementos_tuplos(arg):
    for ele in arg:
        if not isinstance(ele, tuple):
            return False
    return True

"""verifica_tuplos_corretos: universal --> boolean
verifica_tuplos_corretos(lst) verifica se os elementos contidos nos tuplos correspondem ao pedido. E verdadeiro se tal se verificar e falso caso contrario."""
def verifica_tuplos_corretos(arg):
    for ele in arg:
        if not isinstance(ele[0], str) or not e_coordenada(ele[1]):
            return False
    return True
 
"""verifica_grelha_linha: grelha x coordenada --> boolean
verifica_grelha_linha(g, c) verifica se as coordenadas pedidas sao validas. E verdadeiro se tal se verificar e falso caso contrario."""           
def verifica_grelha_linha(g,c):
    linhas = grelha_nr_linhas(g)
    colunas = grelha_nr_colunas(g)
    linha = coord_linha(c)
    coluna = coord_coluna(c)
    direcao = coord_direcao(c)
    resposta = ''
    if linha >= linhas or coluna >= colunas:
        return False
    return True
 
"""verifica_direcao_vertical: grelha, coordenada --> resposta
verifica_direcao_vertical(g, c) verifica se a direcao pedida e vertical, e qual o seu sentido."""    
def verifica_direcao_vertical(g,c):
    resposta = ''    
    if e_sul(coord_direcao(c)):
        linha_sul(g,c)
    if e_norte(coord_direcao(c)):
        resposta = resposta + inverte(linha_sul(g,c))
    return resposta    

"""verifica_direcao_horizontal: grelha, coordenada --> resposta
verifica_direcao_horizontal(g, c) verifica se a direcao pedida e horizontal, e qual o seu sentido."""
def verifica_direcao_horizontal(g,c):
    resposta = ''
    if e_oeste(coord_direcao(c)):
        linha_oeste(g,c)
    if e_leste(coord_direcao(c)):
        resposta = resposta + inverte(linha_oeste(g,c))
    return resposta

"""verifica_direcao_diagonal: grelha, coordenada --> resposta
verifica_direcao_diagonal(g, c)  verifica se a direcao pedida e diagonal, e qual o seu sentido."""
def verifica_direcao_diagonal(g,c):
    resposta = ''
    if e_noroeste(coord_direcao(c)):
        linha_noroeste(g,c)
    if e_sudeste(coord_direcao(c)):
        resposta = resposta + inverte(linha_noroeste(g,c))
    if e_nordeste(coord_direcao(c)):
        linha_nordeste(g,c)
    if e_sudoeste(coord_direcao(c)):
        resposta = resposta + inverte(linha_nordeste(g,c))
    return resposta
    


"""linha_sul: grelha, coordenada --> resposta
linha_sul(g, c) devolve uma linha da grelha g, a partir da coordenada c, com sentido vertical e direcao sul."""
def linha_sul(g,c):
    resposta = ''
    for l in range(grelha_nr_linhas(g)):
        resposta = resposta + grelha_elemento(g, l, c[1])
    return resposta


"""linha_oeste: grelha, coordenada --> resposta
linha_sul(g, c) devolve uma linha da grelha g, a partir da coordenada c, com sentido horizontal e direcao oeste."""
def linha_oeste(g,c):
    resposta = ''
    if e_oeste(direcao):
        for col in range(colunas-1,-1,-1):
            resposta = resposta + grelha_elemento(g,c[0],col)
    return resposta    

"""linha_noroeste: grelha, coordenada --> resposta
linha_noroeste(g, c) devolve uma linha da grelha g, a partir da coordenada c, com sentido diagonal e direcao noroeste"""
def linha_noroeste(g,c):
    reposta = ''
    if e_noroeste(direcao):
        while linha+1 in range(linhas) and coluna+1 in range(colunas):
            linha = linha + 1
            coluna = coluna + 1
        while linha in range(linhas) and coluna in range(colunas):
            resposta = resposta + grelha_elemento(g, linha,coluna)
            linha = linha - 1
            coluna = coluna - 1
    return resposta
    
"""linha_nordeste: grelha, coordenada --> resposta
linha_nordeste(g, c) devolve uma linha da grelha g, a partir da coordenada c, com sentido diagonal e direcao nordeste"""
def linha_nordeste(g,c):
    resposta = ''
    if e_nordeste(coord_direcao(c)):
            while linha + 1 in range(linhas) and coluna -1 in range(colunas):
                linha = linha + 1
                coluna = coluna -1
            while linha in range(linhas) and coluna in range(colunas):
                resposta = resposta + grelha_elemento(g, linha,coluna)
                linha = linha -1
                coluna = coluna + 1   
    return resposta

"""inverte: string --> string
inverte(string) inverte a string."""
def inverte(string):
    return string[len(string)-1::-1]

"""string_para_lista: string --> list
string_para_lista(string) converte uma string numa lista, sendo que um espaco corresponde a separacao de dois elementos."""
def string_para_lista(string):
    return string.split(', ')
    
    

