# Função para realizar a busca em profundidade (DFS) no grafo e gerar o desenho da hierarquia dos nodos pesquisados
def dfs(G, dfs_list, v, depth):
    dfs_list[v] = VISITED  # Marca o nodo como visitado
    output = ""
    for w in range(len(G[v])):  # Percorre todos os nodos adjacentes ao nodo atual
        if G[v][w] == CONNECTED:  # Se houver uma aresta entre os nodos v e w
            output = get_blank_spaces(depth * 2)  # Adiciona espaços de acordo com a profundidade
            output += str(v) + "-" + str(w)  # Adiciona a conexão entre os nodos v e w ao output
            if dfs_list[w] == UNVISITED:  # Se o nodo w não foi visitado ainda
                if f:  # Se for o primeiro nodo a ser visitado na profundidade atual
                    print()
                    f = False
                output += " pathR(G," + str(w) + ")"  # Adiciona a chamada recursiva ao output
            print(output)  # Imprime o output
            if dfs_list[w] == UNVISITED:  # Se o nodo w não foi visitado ainda
                dfs(G, dfs_list, w, depth + 1)  # Chama recursivamente a DFS para o nodo w com uma profundidade aumentada

# Função para criar uma string com espaços em branco
def get_blank_spaces(count):
    s = ""
    for _ in range(count):
        s += " "
    return s

if __name__ == "__main__":
    N = int(input())  # Lê o número de casos de teste
    case_number = 1

    UNVISITED = -1  # Constante para marcar um nodo como não visitado
    VISITED = 1  # Constante para marcar um nodo como visitado
    CONNECTED = 1  # Constante para indicar a existência de uma aresta entre dois nodos
    f = False  # Variável para controlar a impressão de linhas em branco

    # Para cada caso de teste
    for _ in range(N):
        V, E = map(int, input().split())  # Lê a quantidade de vértices e arestas do grafo
        dfs_list = [UNVISITED] * V  # Inicializa a lista de visitados
        G = [[0] * V for _ in range(V)]  # Inicializa a matriz de adjacência do grafo

        # Lê as arestas do grafo e atualiza a matriz de adjacência
        for _ in range(E):
            source, destination = map(int, input().split())
            G[source][destination] = CONNECTED

        print("Caso " + str(case_number) + ":")  # Imprime o número do caso de teste
        # Para cada vértice do grafo
        for i in range(V):
            if dfs_list[i] == UNVISITED:  # Se o vértice ainda não foi visitado
                f = True  # Marca que é o primeiro vértice da profundidade atual
                dfs(G, dfs_list, i, 1)  # Chama a DFS a partir deste vértice
        print()  # Imprime uma linha em branco após cada segmento do grafo
        case_number += 1  # Incrementa o número do caso de teste
