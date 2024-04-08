from collections import deque

def BFS(start, grafo, visitado):
    fila = deque([start])  # Inicializa a fila com o nó inicial
    visitado[start] = True  # Marca o nó inicial como visitado
    movimentos = 0  # Inicializa o contador de movimentos

    # Enquanto houver nós na fila
    while fila:
        tamanho_fila = len(fila)
        # Para cada nó na fila atual
        for _ in range(tamanho_fila):
            atual = fila.popleft()  # Remove o nó da fila
            # Para cada vizinho do nó atual
            for vizinho in grafo[atual]:
                if not visitado[vizinho]:  # Se o vizinho não foi visitado
                    fila.append(vizinho)  # Adiciona o vizinho na fila
                    visitado[vizinho] = True  # Marca o vizinho como visitado
                    movimentos += 1  # Incrementa o contador de movimentos
    return movimentos * 2  # Retorna o número mínimo de movimentos (cada movimento representa ida e volta)

def main():
    T = int(input())  # Número de casos de teste
    for _ in range(T):
        N = int(input())  # Nodo inicial
        V, A = map(int, input().split())  # Quantidade de vértices e arestas
        grafo = [[] for _ in range(V)]  # Inicializa o grafo
        for _ in range(A):
            u, v = map(int, input().split())
            grafo[u].append(v)
            grafo[v].append(u)

        visitado = [False] * V  # Inicializa o array de visitados
        movimentos = BFS(N, grafo, visitado)  # Chama a função BFS para calcular os movimentos
        print(movimentos)  # Imprime o resultado para o caso de teste atual

if __name__ == "__main__":
    main()
