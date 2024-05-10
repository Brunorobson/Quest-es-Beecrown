from collections import deque

# Função para inverter os dígitos de um número
def inverter_digitos(num):
    return int(str(num)[::-1])

# Função para encontrar o número mínimo de apertos de botão para transformar A em B
def min_pressoes_botao(A, B):
    fila = deque([(A, 0)])  # Inicializa a fila com o número inicial e a quantidade de apertos de botão
    visitados = set()  # Conjunto para rastrear os números visitados

    while fila:
        num, pressoes = fila.popleft()  # Remove o primeiro elemento da fila
        if num == B:  # Se o número atual é igual a B, retorna a quantidade de apertos de botão
            return pressoes
        if num in visitados:  # Se o número atual já foi visitado, continue para o próximo número na fila
            continue

        visitados.add(num)  # Marca o número atual como visitado

        # Adiciona os números resultantes dos apertos de botão à fila
        proximo_num = num + 1
        if proximo_num <= B:
            fila.append((proximo_num, pressoes + 1))
        proximo_num = inverter_digitos(num)
        if proximo_num <= B:
            fila.append((proximo_num, pressoes + 1))

# Leitura da entrada
T = int(input("Digite o número de casos de teste: "))

# Processamento dos casos de teste
for _ in range(T):
    A, B = map(int, input().split())
    resultado = min_pressoes_botao(A, B)
    print(resultado)
