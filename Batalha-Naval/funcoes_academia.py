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

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

config_navios = {
    "porta-aviões": {"tamanho": 4, "quantidade": 1},
    "navio-tanque": {"tamanho": 3, "quantidade": 2},
    "contratorpedeiro": {"tamanho": 2, "quantidade": 3},
    "submarino": {"tamanho": 1, "quantidade": 4},
}

for navio, info in config_navios.items():
    tamanho = info["tamanho"]
    quantidade = info["quantidade"]
    
    for i in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
            pos_linha = int(input("Linha: "))
            pos_coluna = int(input("Coluna: "))
            if tamanho > 1:
                orientacao = int(input("[1] Vertical [2] Horizontal > "))
                orientacao = 'vertical' if orientacao == 1 else 'horizontal'
            else:
                orientacao = 'vertical'

            if posicao_valida(frota, pos_linha, pos_coluna, orientacao, tamanho):
                posicoes = define_posicoes(pos_linha, pos_coluna, orientacao, tamanho)
                frota[navio].append(posicoes)
                break
            else:
                print("Esta posição não está válida!")

print(frota)


