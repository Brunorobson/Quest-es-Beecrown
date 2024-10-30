def percurso_posfixo(percurso_prefixo, percurso_infixo):
    if not percurso_prefixo:
        return ""

    raiz = percurso_prefixo[0]
    indice_raiz = percurso_infixo.index(raiz)

    esquerda_infixo = percurso_infixo[:indice_raiz]
    direita_infixo = percurso_infixo[indice_raiz + 1:]

    esquerda_prefixo = percurso_prefixo[1:1 + len(esquerda_infixo)]
    direita_prefixo = percurso_prefixo[1 + len(esquerda_infixo):]

    esquerda_posfixo = percurso_posfixo(esquerda_prefixo, esquerda_infixo)
    direita_posfixo = percurso_posfixo(direita_prefixo, direita_infixo)

    return esquerda_posfixo + direita_posfixo + raiz

import sys

linhas_entrada = sys.stdin.read().strip().splitlines()
casos = int(linhas_entrada[0])

resultados = []

for i in range(1, casos + 1):
    linha = linhas_entrada[i].strip()
    partes = linha.split()
    n_nodos = int(partes[0])
    percurso_prefixo = partes[1]
    percurso_infixo = partes[2]
    
    resultado_posfixo = percurso_posfixo(percurso_prefixo, percurso_infixo)
    resultados.append(resultado_posfixo)

for resultado in resultados:
    print(resultado)
