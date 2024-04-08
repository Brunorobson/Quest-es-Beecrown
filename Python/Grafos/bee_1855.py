def dfs(x, y, mapa, visitados):
    largura = len(mapa[0])
    altura = len(mapa)

    # Verifica se está dentro dos limites do mapa
    if x < 0 or x >= largura or y < 0 or y >= altura:
        return False

    # Verifica se já visitou este ponto
    if visitados[y][x]:
        return False

    # Marca o ponto atual como visitado
    visitados[y][x] = True

    # Verifica se encontrou o baú de obsidiana
    if mapa[y][x] == '*':
        return True

    # Move-se para o próximo ponto de acordo com a direção indicada pela flecha
    if mapa[y][x] == '>':
        return dfs(x + 1, y, mapa, visitados)
    elif mapa[y][x] == '<':
        return dfs(x - 1, y, mapa, visitados)
    elif mapa[y][x] == 'v':
        return dfs(x, y + 1, mapa, visitados)
    elif mapa[y][x] == '^':
        return dfs(x, y - 1, mapa, visitados)
    else:
        return False

def verificar_mapa(mapa):
    largura = len(mapa[0])
    altura = len(mapa)

    # Inicializa a matriz de visitados
    visitados = [[False] * largura for _ in range(altura)]

    # Procura pelo ponto de partida
    for y in range(altura):
        for x in range(largura):
            if mapa[y][x] == '.':
                # Inicia a DFS a partir do ponto de partida
                if dfs(x, y, mapa, visitados):
                    return '*'
                else:
                    return '!'
    return '!'

def main():
    largura = int(input())
    altura = int(input())
    mapa = [input() for _ in range(altura)]

    resultado = verificar_mapa(mapa)
    print(resultado)

if __name__ == "__main__":
    main()