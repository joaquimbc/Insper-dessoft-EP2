def define_posicoes(pos_linha, pos_coluna, orientacao, tamanho):
    lista_resultado = [[pos_linha, pos_coluna]]
    if orientacao == 'vertical':
        for i in range(1, tamanho):
            lista_resultado.append([pos_linha+i, pos_coluna])
    else:
        for i in range(1, tamanho):
            lista_resultado.append([pos_linha, pos_coluna+i])
    return lista_resultado

def preenche_frota(dicio_frota, navio, pos_linha, pos_coluna, orientacao, tamanho):
    lista_resultado = []
    
    if orientacao == 'vertical':
        for i in range(pos_linha, pos_linha+tamanho):
            lista_resultado.append([i, pos_coluna])
    else:
        for i in range(pos_coluna, pos_coluna+tamanho):
            lista_resultado.append([pos_linha, i])
    
    return lista_resultado

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def gera_tabuleiro():
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = gera_tabuleiro()
    
    for navio in frota:
        posicoes = frota[navio]
        for posicao in posicoes:
            for linha in posicao:
                tabuleiro[linha[0]][linha[1]] = 1
    
    return tabuleiro


def afundados(frota, tabuleiro):
    navios_afundados = 0
    for tipo, posicoes in frota.items():
        for navio in posicoes:
            afundado = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundado = False
                    
            if afundado:
                navios_afundados += 1
    return navios_afundados

def fora_tabuleiro(posicao):
    if 0 <= posicao[0] < 10 and 0 <= posicao[1] < 10:
        return False
    return True

def posicao_valida(dicio_navios, pos_linha, pos_coluna, orientacao, tamanho):
    
    posicao_navio = define_posicoes(pos_linha, pos_coluna, orientacao, tamanho)
    for coord_navio in posicao_navio:
        if fora_tabuleiro(coord_navio):
            return False
    
        for navio in dicio_navios.values():
            for posicao in navio:
                for coordenadas in posicao:
                    if coordenadas == coord_navio:
                        return False
    return True



