from collections import defaultdict

# Função para ler a entrada
def ler_entrada():
    while True:
        N = int(input())  # Número de pessoas no grupo
        if N == 0:
            break
        amigos = defaultdict(list)
        for i in range(1, N + 1):
            amigos[i] = list(map(int, input().split()[:-1]))  # Lista de amigos de cada pessoa
        spam = []  # Lista de mensagens de SPAM
        while True:
            entrada = input().split()
            if entrada == ['0']:
                break
            P, T1, T2, A1, A2, A3 = int(entrada[0]), int(entrada[1]), int(entrada[2]), entrada[3], entrada[4], entrada[5]
            spam.append((P, T1, T2, A1, A2, A3))
        nomes = [input() for _ in range(N)]  # Nomes das pessoas
        yield N, amigos, spam, nomes

# Função para determinar os atributos de cada pessoa
def determinar_atributos(N, amigos, spam, nomes):
    atributos = defaultdict(list)
    for pessoa in range(1, N + 1):
        visitados = set()  # Conjunto de amigos já visitados para evitar ciclos
        for amigo in amigos[pessoa]:
            fila = [(amigo, 1)]  # Inicializa a fila com os amigos da pessoa e o número de mensagens de SPAM encaminhadas por eles
            while fila:
                atual, qtd_spam = fila.pop(0)  # Remove o primeiro da fila
                visitados.add(atual)
                for P, T1, T2, A1, A2, A3 in spam:
                    if atual == P:
                        if qtd_spam < T1:
                            atributos[pessoa].append(A1)
                        elif T1 <= qtd_spam < T2:
                            atributos[pessoa].append(A2)
                        else:
                            atributos[pessoa].append(A3)
                        break
                for prox_amigo in amigos[atual]:
                    if prox_amigo not in visitados:
                        fila.append((prox_amigo, qtd_spam + 1))
    return atributos

# Função para imprimir os atributos de cada pessoa
def imprimir_atributos(atributos, nomes):
    for pessoa, atribs in atributos.items():
        print(f"{nomes[pessoa - 1]}: {' '.join(atribs)}")

# Função principal
def main():
    for N, amigos, spam, nomes in ler_entrada():
        atributos = determinar_atributos(N, amigos, spam, nomes)
        imprimir_atributos(atributos, nomes)

if __name__ == "__main__":
    main()
