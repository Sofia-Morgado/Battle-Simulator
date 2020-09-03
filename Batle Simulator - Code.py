# Sofia da Silva Morgado nr195675 

##########################################################################
########################### TAD POSICOES #################################
##########################################################################
                 
                 #cria_posicao: int -> posicao(lista)
                 
         # cria_copia_posicao: posicao(lista) -> posicao(lista)
         
                  # obter_pos_x: posicao(lista) -> int
                  
                  # obter_pos_y: posicao(lista) -> int
                  
                  # eh_posicao: universal -> booleano
                  
        #posicoes_iguais: posicao(lista) x posicao(lista) -> booleano 
        
                   #posicao_para_str: posicao -> str 
                   
          # ordenar_posicoes: tuplo posicoes -> tuplo posicoes
                   
         #obter_posicoes_adjacentes: posicao -> tuplo de posicoes 


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                           Construtores                                 #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def cria_posicao(x,y):
    '''
    A funcao cria_posicao devolve a posicao correspondentes as coordenadas do argumento.
    
    cria_posicao: x x y (int) -> posicao 
    '''    
    if (isinstance(x, int) and isinstance(y,int) and x>=0 and y>=0):
        return [x,y]
    else:
        raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(pos):
    '''
    A funcao cria_copia_posicao devolve a copia da posicao, dada no argumento. 
    
    cria_copia_posicao: posicao -> posicao 
    ''' 
    return cria_posicao(pos[0], pos[1])

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                            Seletores                                   #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
def obter_pos_x(pos):
    '''
    A funcao obter_pos_x devolve a componente x da posicao da unidade do argumento.
    
    obter_pos_x: posicao -> int (x)
    '''
    return pos[0]

def obter_pos_y(pos):
    '''
    A funcao obter_pos_y devolve a componente y da posicao da unidade do argumento.
    
    obter_pos_y: posicao -> int (y)
    '''
    return pos[1]

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                          Reconhecedores                                #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def eh_posicao(pos):
    '''
    A funcao eh_posicao devolve True caso o seu argumento seja uma posicao e False caso contrario. 
    
    eh_posicao: posicao -> booleano 
    '''
    
    return (isinstance(pos, list) and 2== len(pos)) and (isinstance( obter_pos_x(pos), int) and isinstance(obter_pos_y(pos),int) and obter_pos_x(pos)>=0 and obter_pos_y(pos)>=0)
    
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                              Testes                                    #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def posicoes_iguais(p1,p2):
    '''
    A funcao posicoes_iguais devolve True caso as posicoes dadas sejam iguais e False caso contrario. 
    
    posicoes_iguais: posicao _ posicao -> booleano
    '''
    return (obter_pos_x(p1)==obter_pos_x(p2) and obter_pos_y(p1)==obter_pos_y(p2))
        

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                          Transformadores                               #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
def posicao_para_str(pos):
    '''
    A funcao posicao_para_str devolve a cadeia de caracteres '[x, y]' que representa as coordenadas do seu argumento (posicao).

    posicao_para_str: posicao -> '[x, y]'
    ''' 
    return str(tuple(pos))

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD POSICOES                                 #
#------------------------------------------------------------------------#
#                            Alto Nivel                                  #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def ordenar_posicoes(tup_pos):
    '''
    A funcao ordenar_posicoes devolve um tuplo com as posicoes ordenadas segundo a ordem de leitura do mapa.
    
    obter_posicoes_adjacentes: tuplo posicao -> tuplo posicao 
    '''    
    return tuple(sorted(tup_pos, key=lambda pos: (obter_pos_y(pos), obter_pos_y(pos))))

def obter_posicoes_adjacentes(pos):
    '''
    A funcao obter_posicoes_adjacentes devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a ordem de leitura de um labirinto

    obter_posicoes_adjacentes: posicao -> lista de posicoes   
    '''
    lista = []
    
    x = obter_pos_x(pos)
    y = obter_pos_y (pos)
    
    acima = [x,y-1]
    direita = [x-1,y]
    esquerda = [x+1,y]
    baixo = [x,y+1]
    
    if x == 0 and y == 0:
        lista += [esquerda, baixo]
        return tuple(lista)
    
    elif x == 0:
        lista += [acima,esquerda,baixo]
        return tuple(lista)
    
    elif y == 0:
        lista += [direita,esquerda,baixo]
        return tuple(lista)
    
    else:
        lista += [acima,direita,esquerda,baixo]
        return tuple(lista)
        
##########################################################################
########################### TAD UNIDADES #################################
##########################################################################
    #cria_unidade: posicao(lista) x vida(int) x forca de ataque(int) x exercito(str) -> unidade(lista) 
    
              #cria_copia_unidade: unidade -> unidade 
              
              #obter_posicao: unidade -> posicao 
              
              # obter_exercito: unidade -> str
              
              # obter_forca: unidade -> N
              
              # obter_vida: unidade -> N 
              
              #  obter_exercito: unidade -> str
              
              # muda_posicao: unidade x posicao -> unidade
              
              # remove_vida: unidade x N -> unidade
              
              #  eh_unidade: universal -> booleano
              
              # unidades_iguais: unidade x unidade -> booleano 
              
              #  unidade_para_char: unidade -> str
              
              # unidade_para_str: unidade -> str
              
              # unidade_ataca: unidade x unidade -> booleano
              
              # ordenar_unidades: tuplo unidades -> tuplo unidades
              
              
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                           Construtores                                 #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def cria_unidade(p,v,f,str1):
    '''
    A funcao cria_unidade devolve uma unidade, caracterizada pelos argumentos - posicao, vida, forca de ataque e pelo exercito a que pertence.

    cria_unidade: posicao x vida x forca de ataque x exercito -> unidade 
    ''' 
    if eh_posicao(p) and isinstance(v, int) and isinstance(f, int) and v>0 and f>0 and isinstance(str1, str) and str1 != '':
        uni = [p,v,f,str1]
        return uni
    else:
        raise ValueError('cria_unidade: argumentos invalidos')

def cria_copia_unidade(uni):
    '''
    A funcao cria_copia_unidade devolve a copia da unidade, dada no argumento. 
    
    cria_copia_unidade: unidade -> unidade
    ''' 
    return cria_unidade(cria_copia_posicao(uni[0]),uni[1],uni[2],uni[3])

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                             Seletores                                  #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def obter_posicao(uni):
    '''
    A funcao obter_posicao devolve a posicao do argumento. 
    
    obter_posicao: unidade -> posicao
    ''' 
    return uni[0]

def obter_exercito(uni):
    '''
    A funcao obter_exercito devolve a cadeia de carateres correspondente ao exercito do argumento. 
    
    obter_exercito: unidade -> string
    ''' 
    return uni[3]    

def obter_forca(uni):
    '''
    A funcao obter_forca devolve o valor corresponde a forca de ataque da unidade
    
    obter_forca: unidade -> forca
    '''     
    return uni[2]

def obter_vida(uni):
    '''
    A funcao obter_vida devolve o valor corresponde a vida da unidade
    
    obter_vida: unidade -> vida
    '''        
    return uni[1]    

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                           Modificadores                                #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def muda_posicao(u, p):
    '''
    A funcao muda_posicao devolve a unidade cuja posicao corresponde ao seu segundo argumento. 
    
    muda_posicao: unidade x posicao -> unidade
    '''        
    u[0] = p 
    return u

def remove_vida (u,v):
    '''
    A funcao remove_vida devolve a unidade cujo valor de vida e resultado do valor de vida anterior subtraindo o segundo argumento. 
    
    remove_vida: unidade x v -> unidade
    '''     
    u[1] -= v
    return u

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                           Reconhecedor                                 #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def eh_unidade(u):
    return isinstance(u, list) and len(u)==4 and eh_posicao(obter_posicao(u)) and isinstance(obter_vida(u), int) and isinstance(obter_forca(u), int) and obter_vida(u)>0 and obter_forca(u)>0 and isinstance(obter_exercito(u), str) and obter_exercito(u)!= '' 

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                              Teste                                     #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def unidades_iguais(u1, u2):
    '''
    A funcao unidades_iguais devolve True se as unidades forem iguais e False caso contrario. 
    
    muda_posicao: unidada x unidade -> valor logico
    '''       
    return (obter_pos_x(obter_posicao(u1)) == obter_pos_x(obter_posicao(u2)) and obter_pos_y(obter_posicao(u1)) == obter_pos_y(obter_posicao(u2)) and obter_vida(u1)==obter_vida(u2) and obter_forca(u1)==obter_forca(u2) and obter_exercito(u1)== obter_exercito(u2))
        
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                          Transformadores                               #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def unidade_para_char (uni):
    '''
    A funcao unidade_para_char devolve a primeira letra do exercito a que corresponde a unidade.  
    
    unidade_para_char: unidada -> primeira letra do exercito
    '''       
    c = ord(obter_exercito(uni)[0]) 
    
    if 65 <= c <= 90: #se a primeira letra for maiscula
        return chr(c) 
    
    elif 97 <= c <= 122: #se a primeira letra for minuscula
        return chr(c-32)
    
    else:
        raise ValueError ('unidade_para_char: nome do exercito nao e valido')

def unidade_para_str(uni):
    '''
    A funcao unidade_para_char devolve a primeira letra do exercito a que corresponde a unidade.  
    
    unidade_para_char: unidada -> primeira letra do exercito
    '''
    return str(unidade_para_char(uni)) + str([obter_vida(uni), obter_forca(uni)]) + '@' + str(tuple(obter_posicao(uni)))

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                           TAD UNIDADES                                 #
#------------------------------------------------------------------------#
#                            Alto Nivel                                  #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def unidade_ataca (u1, u2):
    '''
    A funcao unidade_ataca retira o correspondente a forca de ataque do primeiro argumetno aos pontos de vida do segundo argumento. A funcao devolve True se a unidade u2 for destruida ou False caso contrario. 
    
    unidade_ataca: unidada x unidade -> booleano
    '''    
    u2 = remove_vida(u2,obter_forca(u1))
    
    #foi eliminada
    if obter_vida(u2) <= 0:
        return True
    
    #ainda esta viva
    else:
        return False

def ordenar_unidades(tup_uni):
    '''
    A funcao ordenar_unidades devolve um tuplo contendo as mesmas unidades do tuplo fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto.
    
    ordenar_unidades: tuplo de unidades-> tuplo unidades
    '''      
    return tuple(sorted(tup_uni, key=lambda uni: (obter_pos_y(obter_posicao(uni)), obter_pos_x(obter_posicao(uni)))))
                            
##########################################################################
########################### TAD MAPA #####################################
##########################################################################

#cria_mapa: tuplo(dimensao) x tuplo(paredes internas) x tuplo(exercito 1) x tuplo(exercito 2) -> lista (mapa)

# cria_copia_mapa: mapa -> mapa

# obter_tamanho: mapa -> tuplo 

# obter_nome_exercitos: mapa -> tuplo 

# obter_unidades_exercito: mapa x str -> tuplo unidades

# obter_todas_unidades: mapa -> tuplo

# obter_unidade: mapa x posicao -> unidade 

# eliminar_unidade: mapa x unidade -> mapa 

# mover_unidade: mapa x unidade x posicao -> mapa

# eh_posicao_unidade: mapa x posicao -> booleano 

# eh_posicao_corredor: mapa x posicao -> booleano

# eh_posicao_parede: mapa  x posicao -> booleano

# mapas_iguais: mapa x mapa -> booleano 

# mapa_para_str: mapa -> str 

# obter_inimigos_adjacentes: mapa x unidade ->  tuplo unidades

# obter_movimento: mapa x unidade -> posicao

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                          Construtores                                  #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def cria_mapa (d, w, e1, e2):
    '''
    A funcao cria_mapa recebe um tuplo d, dimensoes do mapa,  um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao dos limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do mesmo exercito, e um tuplo e2 de um ou mais unidades de um outro exercito; e devolve o mapa que representa internamente o labirinto e as unidades presentes.
    
    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    '''     
    #verificar dimensoes 
    if not (len(d)== 2 and isinstance(d, tuple) and isinstance(d[0], int) and isinstance(d[1], int) and d[0]>=3 and d[1]>=3):
        raise ValueError('cria_mapa: argumentos invalidos')
    
    #verificar exercitos
    #sao tuplos
    if not (isinstance(e1, tuple) and e1 != () and isinstance(e2, tuple)  and e2 != ()):
        raise ValueError('cria_mapa: argumentos invalidos')      
    
    #e1 sao unidades 
    for u in range(len(e1)):
        if not eh_unidade(e1[u]):
            raise ValueError('cria_mapa: argumentos invalidos')    
    
    #e2 sao unidades
    for u in range(len(e2)):
        if not eh_unidade(e2[u]):
            raise ValueError('cria_mapa: argumentos invalidos')
                    
    for n in range(len(w)):
        #sao paredes dentro do mapa
        if not (0<obter_pos_x(w[n])<(d[0]-1) and 0<obter_pos_y(w[n])<(d[1]-1)):
            raise ValueError('cria_mapa: argumentos invalidos') 
             
        
    #unidades dos exercitos tem de ser diferentes 
    for p1 in range(len(e1)):
        for p2 in range(len(e2)):
            if unidades_iguais(e1[p1], e2[p2]):
                raise ValueError('cria_mapa: argumentos invalidos')
    
    # criar um tuplo 4 para os nomes dos exercitos
    nome_e1 = e1[0][3]
    nome_e2 = e2[0][3]
    if nome_e1 < nome_e2:
        nomes = (nome_e1, nome_e2)
    else:
        nomes = (nome_e2, nome_e1)    
    
    return [d, w, e1, e2, nomes]

 
def cria_copia_mapa (mapa):
    '''
    A funcao cria_copia_mapa recebe um mapa e devolve uma nova copia do mapa.
    
    cria_copia_mapa: mapa -> mapa
    '''     
    return cria_mapa(mapa[0], mapa[1], tuple(cria_copia_unidade(u) for u in mapa[2]), tuple(cria_copia_unidade(u) for u in mapa[3]))


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                            Seletores                                   #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def obter_tamanho(mapa):
    '''
    A funcao obter_tamanho devolve um tuplo de dois valores inteiros correspondendo o primeiro deles a dimensao x e o segundo a dimensao Ny do mapa. 
    
    obter_tamanho: mapa -> tuplo
    '''        
    return mapa[0]


def obter_paredes(m):
    '''
    A funcao obter_paredes devolve um tuplo com as paredes do mapa.
    
    obter_paredes: mapa -> tuplo
    '''        
    return m[1]


def obter_e1(m):
    '''
    A funcao obter_e1 devolve o primeiro exercito do mapa. 
    
    obter_e1: mapa -> tuplo
    '''        
    return m[2]


def obter_e2(m):
    '''
    A funcao obter_e2 devolve o segundo exercito do mapa. 
    
    obter_e2: mapa -> tuplo
    '''        
    return m[3]


def obter_nome_e1(m): 
    return m[4][0]


def obter_nome_e2(m):            
    return m[4][1]


def obter_nome_exercitos(m):
    '''
    A funcao obter_nome_exercitos devolve um tuplo ordenado com duas cadeias de caracteres correspondendo aos nomes dos exercitos do mapa.
    
    obter_nome_exercitos: mapa -> tuplo
    ''' 
    
    return m[4]
       

def obter_unidades_exercito(m, e):
    '''
    A funcao obter_unidades_exercito  devolve um tuplo contendo as unidades do mapa pertencentes ao exercito indicado pelo segundo argumento, ordenadas em ordem de leitura do labirinto. 
    
    cria_copia_mapa: mapa x str -> tuplo unidades
    '''        
    # se e o exercito 1
    if len(m[2]) > 0 and m[2][0][3] == e:
        return tuple(ordenar_unidades(obter_e1(m)))
    
    # se e o exercito 2
    if len(m[3]) > 0 and m[3][0][3]== e:
        return tuple(ordenar_unidades(obter_e2(m)))
    
    return ()
  
  
def obter_todas_unidades(mapa):
    '''
    A funcao obter_todas_unidades devolve um tuplo contendo todas as unidades do mapa, ordenadas em ordem de leitura do labirinto.
    
    obter_todas_unidades: mapa -> tuplo
    '''        
    return ordenar_unidades(mapa[2]+ mapa[3])


def obter_unidade(m, p):
    '''
    A funcao obter_unidade  devolve a unidade do mapa que se encontra na posicao p, indicada pelo segundo argumento. 

    obter_unidade: mapa x posicao -> unidade
    '''        
    todas_uni = obter_todas_unidades(m)
    
    for i in range(len(todas_uni)):
        # se a posicao for igual a dada, entao retorna a unidade
        if posicoes_iguais(obter_posicao(todas_uni[i]), p):
            return todas_uni[i]
        

def obter_todas_posicoes(m):
    '''
    A funcao obter_todas_posicoes recebe um mapa e devolve um tuplo com todas as posicoes ocupadas pelos exercitos
    
    obter_todas_posicoes: mapa -> tuplo de posicoes
    '''
    #obtermos todas as unidades
    tup_uni = obter_todas_unidades(m)
    res = []
    
    for i in range(len(tup_uni)):
        #obtermos todas as posicoes
        res += [obter_posicao(tup_uni[i])]
        
    return ordenar_posicoes(res)


def obter_todas_posicoes_com_paredes(m):
    '''
    A funcao obter_todas_posicoes_com_paredes recebe um mapa e devolve um tuplo com todas as pocioes ocupadas por unidades dos exercitos ou por paredes, que nao as dos limites exteriores. 
    
    obter_todas_posicoes_com_paredes: mapa -> tuplo de posicoes
    '''        
    res = list(obter_todas_posicoes(m)) + list(obter_paredes(m))
    return ordenar_posicoes(res)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                          Modificadores                                 #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


def eliminar_unidade(m, u):
    '''
    A funcao eliminar_unidade modifica destrutivamente o mapa m eliminando a unidade u do mapa e deixando livre a posicao  onde se encontrava a unidade. Devolve o proprio mapa.
    
    eliminar_unidade: mapa x unidade -> mapa
    '''       
    e1 = obter_e1(m)
    e2 = obter_e2(m)
    
    #unidade esta no e1
    if m[2][0][3] == obter_exercito(u):
    
    #todas as unidades do e1
        list_e1 = list(e1)
        for i in range(len(list_e1)):
            # se a unidade e igual a unidade dada
            if unidades_iguais(list_e1[i], u):
                list_e1.remove(list_e1[i])
                new_e1 = tuple(list_e1)
                m[2] = new_e1 # substituimos o exercito
                return m                
         
    #unidade esta no e2
    else:
        #todas as unidades do e2
        list_e2 = list(e2)
        for i in range(len(list_e2)):
            # se a unidade e igual a unidade dada
            if unidades_iguais(list_e2[i], u):
                list_e2.remove(list_e2[i])
                new_e2 = tuple(list_e2)
                m[3] = new_e2 # substituimos o exercito
                return m                


def mover_unidade(m, u, p):
    '''
    A funcao mover_unidade devolve o mapa cuja posicao da unidade foi alterada e a anterior foi deixada livre. 
    
    mover_unidade: mapa x unidade x posicao -> mapa
    '''      
    #procuramos pelo index, a unidade cuja posicao seja a dada e mudamos a posicao
    u[u.index(obter_posicao(u))] = p
    
    return m 
    
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                          Reconhecedores                                #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def eh_posicao_unidade(m, p):
    '''
    A funcao eh_posicao_unidade devolve True apenas no caso da posicao p do mapa estar ocupada por uma unidade.  
    
    eh_posicao_unidade: mapa x posicao -> booleano
    '''       
    return obter_unidade(m, p) in obter_todas_unidades(m)
    
    
def eh_posicao_corredor(m, p):
    '''
    A funcao eh_posicao_corredor devolve True apenas no caso da posicao p do mapa corresponder a um corredor no labirinto.  
    
    eh_posicao_corredor: mapa x posicao -> booleano
    '''     
    #esta dentro do mapa
    if 0<obter_pos_x(p)<(obter_tamanho(m)[0]-1) and 0<obter_pos_y(p)<(obter_tamanho(m)[1]-1):
        return not eh_posicao_parede(m,p)
    else:
        return False
                      
                      
def eh_posicao_parede (m, p):
    '''
    A funcao eh_posicao_parede devolve True apenas no caso da posicao p do mapa corresponder a uma parede do labirinto.  
    
    eh_posicao_parede: mapa x posicao -> booleano
    '''     
    #parede pode ser interna ou dos limites
    w = obter_paredes(m)
    
    return (p in w) or (obter_pos_x(p)==0 or obter_pos_x(p)==(obter_tamanho(m)[0]-1) or obter_pos_y(p)==0 or obter_pos_y(p)==(obter_tamanho(m)[1]-1))

        
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                             Testes                                     #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def mapas_iguais(m1, m2):
    '''
    A funcao mapas_iguais devolve True se o primeiro argumento e o segundo argumentos forem mapas iguais.
    
    mapas_iguais: mapa x mapa -> booleano
    '''     
    
    return (obter_tamanho(m1)==obter_tamanho(m2) and obter_paredes(m1)==obter_paredes(m2) and ((obter_e1(m1)==obter_e1(m2) and obter_e2(m1)==obter_e2(m2)) or obter_e2(m1)==obter_e1(m2) and obter_e2(m1)==obter_e1(m2)))


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                           Transformadores                              #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def mapa_para_str(m):
    '''
    A funcao mapas_para_str devolve uma cadeia de caracteres que representa o mapa com as unidades representadas pela sua representacao externa.

    mapas_para_str: mapa -> str
    '''      
    colunas = (obter_tamanho(m))[0]
    linhas = (obter_tamanho(m))[1]
    mapa = ''
    all_pos = ordenar_posicoes(obter_todas_posicoes_com_paredes(m))
    
    for i in range(linhas):
        #primeira e ultima linha sao #
        if i == 0 or i==(linhas-1):
            mapa += str('#'*colunas)
            mapa += str('\n')

        else:
            for j in range(colunas):
                #primeira e ultima coluna sao #
                if j==0 or j==(colunas-1):
                    mapa += str('#')
                    
                else: 
                    #verifica se e uma posicao livre
                    if not (eh_posicao_unidade(m, [j, i]) or eh_posicao_parede(m, [j, i])):
                        mapa += str('.') 
                    
                    #se nao, e uma parede ou uma unidade
                    else:
                        for c in range(len(all_pos)):
                            if obter_pos_x(all_pos[c])== j and obter_pos_y(all_pos[c])== i:
                                
                                #parede
                                if eh_posicao_parede(m, all_pos[c]):
                                    mapa += str('#')
                                
                                #unidade
                                elif eh_posicao_unidade(m, all_pos[c]) and not eh_posicao_parede(m, all_pos[c]):
                                    uni = obter_unidade(m, all_pos[c])
                                    mapa += unidade_para_char(uni)
                                           
            #no final de cada linha, adiciona paragrafo
            mapa += str('\n')
    mapa = ''.join(mapa)
    return mapa[:-1]    

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                            TAD MAPA                                    #
#------------------------------------------------------------------------#
#                           Alto Nivel                                   #
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

def obter_inimigos_adjacentes(m, u):
    '''
    A funcao obter_inimigos_adjacentes devolve um tuplo contendo as unidades inimigas adjacentes a unidade u de acordo com a ordem de leitura do labirinto.  
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades
    '''  
    # obtermos as posicoes adjacentes
    adj = obter_posicoes_adjacentes(obter_posicao(u))
    res = []
    e = obter_exercito(u)
    for pos in adj:
        if eh_posicao_unidade(m, pos):
            #se e uma unidade valida, vamos obte-la
            uni_adj = obter_unidade(m, pos)
            #se a unidade e o exercito inimigo
            if obter_exercito(uni_adj) != e:
                res += [uni_adj]
    return tuple(res)    
    
    
    
def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)




#########################################################################
#                       FUNCOES ADICIONAIS                              #
#########################################################################

# calcula_pontos: mapa x str -> int 

# simula_turno: mapa -> mapa 

# simula_batalha: str x booleano -> str 

def calcula_pontos(m, nome_e):
    '''
    A funcao auxiliar calcula_pontos devolve a pontuacao correspondente ao exercito, segundo argumento. 

    calcula_pontos: mapa x str -> int
    '''    
    soma = 0
    #obtermos todas as unidades do exercito
    tup_uni = obter_unidades_exercito(m, nome_e)

    #vamos somar os pontos de vida de todas as unidades desse exercito
    for i in range(len(tup_uni)):
        vida = obter_vida(tup_uni[i])
        soma += vida
    
    return soma


def simula_turno(m): 
    '''
    A funcao auxiliar simula_turno modifica o mapa fornecido como argumento de acordo com a simulacao de um turno de batalha completo, em que acada unidade realiza um movimento e um ataque, e devolve o proprio mapa.

    simula_turno: mapa -> mapa
    '''    
    ######################
    ## Funcao auxiliar  ##
    ######################
    def unidade_nao_parede(m, u):
        paredes_int = obter_paredes(m)
        return (0<obter_pos_x(u)<(obter_tamanho(m)[0]-1) and 0<obter_pos_y(u)<(obter_tamanho(m)[1]-1) and u not in paredes_int)

    #obtermos todas as unidades do mapa ordenadas
    todas_uni = list(ordenar_unidades(obter_todas_unidades(m)))
    
    i = 0
    while i in range(len(todas_uni)):
        p = obter_movimento(m, todas_uni[i])
        # p so se move se n for uma parede interna ou externa
        if unidade_nao_parede(m, p) and (obter_e1(m)!=() and obter_e2(m)!=()):
            m = mover_unidade(m, todas_uni[i], p) 
             
        #obtermos as unidade do exercito inimido
        adj = obter_inimigos_adjacentes(m, todas_uni[i])
        adj = list(adj)
        
        if adj != []:
            #vamos atacar a adjacente inimiga
            adj[0] = remove_vida(adj[0], obter_forca(todas_uni[i]))
            if obter_vida(adj[0]) <= 0:
                eliminar_unidade(m, adj[0])
                #remove a unidade eliminada do tuplo com todas as unidades
                #que estamos a iterar
                todas_uni.remove(adj[0]) 
                i -= 1
        
        i += 1
                
    return m

def simula_batalha(str1, b):
    '''
    A funcao auxiliar simula_batalha  simula uma batalha completa, que termina quando um dos exercitos vence - devolve o nome do exercito vencedor - ou entao quando empatarem. Ha dois modos de jogo, caso o segundo argumento for True, mostra-se todos os mapas e pontuacoes ate ao final, mas, se for False, apenas mostra o mapa e a pontuacao no inicio e apos o fim do ultimo turno da batalha. 

    simula_batalha: str x booleano -> str
    '''    
    #vamos abrir o ficheiro e colocar a informacao em variaveis
    fich = open(str1, 'r')
    d = eval(fich.readline())
    e1 = eval(fich.readline())
    e2 = eval(fich.readline())
    w = eval(fich.readline())
    p_e1 = eval(fich.readline())
    p_e2 = eval(fich.readline())
    
    nome_e1 = e1[0]
    nome_e2 = e2[0]
    
    #vamos criar as paredes internas, os exercitos e o mapa
    r =[]
    for i in range(len(w)):
        r += [cria_posicao(obter_pos_x(w[i]), obter_pos_y(w[i]))]
    w = r
        
    e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), e1[1], e1[2], e1[0]) for p in p_e1) 
    e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), e2[1], e2[2], e2[0]) for p in p_e2) 
    
    m1 = cria_mapa(d, w, e1, e2)
    
    m2 = cria_copia_mapa(m1)
    #'a' e uma flag de controlo para o empate
    a = True

    print(mapa_para_str((m1)))
    print('[ '+ nome_e1 + ':'+ str(calcula_pontos(m1,nome_e1)) + ' '  + nome_e2 + ':' + str(calcula_pontos(m1,nome_e2)) + ' ]' )  
    
    while (calcula_pontos(m1, nome_e1)>=0 and calcula_pontos(m1, nome_e2)>=0):
        # se True, vai imprimir todos os mapas enquanto faz a simulacao
        if b:
            print(mapa_para_str(simula_turno(m1)))
            print('[ '+ nome_e1 + ':'+ str(calcula_pontos(m1,nome_e1)) + ' ' + nome_e2 + ':' + str(calcula_pontos(m1,nome_e2)) + ' ]' ) 
            
            #verifica se e empate
            if a == False and (mapas_iguais(m1, m2) and (calcula_pontos(m1, nome_e1)== calcula_pontos(m2, nome_e1) and calcula_pontos(m1, nome_e2)== calcula_pontos(m2, nome_e2))):
                return 'EMPATE' 
            
            #exercito 2 ganhou 
            if calcula_pontos(m1, nome_e1)<=0:
                return  str(nome_e2)
            
            #exercito 1 ganhou   
            if calcula_pontos(m1, nome_e2)<=0:
                return str(nome_e1) 
            
            m2 = cria_copia_mapa(m1)
            a = False
    
        else:
            # b = False, so simula os turnos, ate dar empate ou uma dos exercitos vence, ai vai imprimir o mapa
            
            simula_turno(m1)
            
            #se der empate
            if a == False and mapas_iguais(m1, m2) and  (calcula_pontos(m1, nome_e1)== calcula_pontos(m2, nome_e1) and calcula_pontos(m1, nome_e2)== calcula_pontos(m2, nome_e2)):
                print(mapa_para_str((m1)))
                print('[ '+ nome_e1 + ':'+ str(calcula_pontos(m1,nome_e1)) + ' '  + nome_e2 + ':' + str(calcula_pontos(m1,nome_e2)) + ' ]' )             
                return 'EMPATE' 
            
            #exercito 2 ganha
            if calcula_pontos(m1, nome_e1)<=0:
                print(mapa_para_str((m1)))
                print('[ '+ nome_e1 + ':'+ str(calcula_pontos(m1,nome_e1)) + ' '  + nome_e2 + ':' + str(calcula_pontos(m1,nome_e2)) + ' ]' )             
                return str(nome_e2)
            
            #exercito 1 ganha
            if calcula_pontos(m1, nome_e2)<=0:
                print(mapa_para_str((m1)))
                print('[ '+ nome_e1 + ':'+ str(calcula_pontos(m1,nome_e1)) + ' '  + nome_e2 + ':' + str(calcula_pontos(m1,nome_e2)) + ' ]' )         
                return str(nome_e1) 
            
            m2 = cria_copia_mapa(m1)
            a = False       