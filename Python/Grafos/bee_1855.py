
from collections import deque

# Função para verificar se o mapa é válido
def mapa_valido(mapa):
    largura = len(mapa[0])
    altura = len(mapa)
    start = None
    
    # Encontra o ponto de partida
    for i in range(altura):
        for j in range(largura):
            if mapa[i][j] == '>':
                start = (i, j)
                break
        if start:
            break
    
    if not start:
        return False
    
    visited = set()
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        visited.add((x, y))
        
        if mapa[x][y] == '*':
            return True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direções possíveis: direita, esquerda, baixo, cima
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < altura and 0 <= ny < largura and mapa[nx][ny] != '.' and (nx, ny) not in visited:
                queue.append((nx, ny))
    
    return False

# Leitura da entrada
largura = int(input())
altura = int(input())
mapa = [input() for _ in range(altura)]

# Verificação se o mapa é válido
if mapa_valido(mapa):
    print("*")  # Mapa válido
else:
    print("!")  # Mapa inválido
