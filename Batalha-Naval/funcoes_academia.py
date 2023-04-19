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


def preenche_frota(dicio_frota, navio, pos_linha, pos_coluna, orientacao, tamanho):
   
   pos_novo_navio = define_posicoes(pos_linha, pos_coluna, orientacao, tamanho)
   
   if dicio_frota != {}:
    if navio not in dicio_frota.keys():
       dicio_frota[navio] = []
    temp = dicio_frota[navio]
    temp.append(pos_novo_navio)
    dicio_frota[navio] = temp
   else:
    dicio_frota[navio] = [pos_novo_navio]
   return dicio_frota