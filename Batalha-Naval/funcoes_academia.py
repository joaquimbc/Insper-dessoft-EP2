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


