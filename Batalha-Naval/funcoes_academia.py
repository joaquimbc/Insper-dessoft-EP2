def define_posicoes(pos_linha, pos_coluna, orientacao, tamanho):

    lista_resultado = [[pos_linha, pos_coluna]]

    if orientacao == 'vertical':
      i = pos_linha
      j = 1
      while j < tamanho:
          lista_resultado.append([i+1, pos_coluna])
          i += 1
          j += 1
      return lista_resultado
    
    i = pos_coluna
    j = 1
    while j < tamanho:
       lista_resultado.append([pos_linha, i+1])
       i += 1
       j += 1
    return lista_resultado