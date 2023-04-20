def preenche_frota(dicio_frota, navio, pos_linha, pos_coluna, orientacao, tamanho):
    lista_resultado = []
    
    if orientacao == 'vertical':
        for i in range(pos_linha, pos_linha+tamanho):
            lista_resultado.append([i, pos_coluna])
    else:
        for i in range(pos_coluna, pos_coluna+tamanho):
            lista_resultado.append([pos_linha, i])
    
    return lista_resultado

