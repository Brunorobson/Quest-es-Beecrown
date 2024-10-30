class TreeNode:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.val = chave

def inserir(raiz, chave):
    if raiz is None:
        return TreeNode(chave)
    else:
        if chave < raiz.val:
            raiz.esquerda = inserir(raiz.esquerda, chave)
        else:
            raiz.direita = inserir(raiz.direita, chave)
    return raiz

def percurso_pre_ordem(raiz):
    return [raiz.val] + percurso_pre_ordem(raiz.esquerda) + percurso_pre_ordem(raiz.direita) if raiz else []

def percurso_in_ordem(raiz):
    return percurso_in_ordem(raiz.esquerda) + [raiz.val] + percurso_in_ordem(raiz.direita) if raiz else []

def percurso_pos_ordem(raiz):
    return percurso_pos_ordem(raiz.esquerda) + percurso_pos_ordem(raiz.direita) + [raiz.val] if raiz else []

import sys

linhas_entrada = sys.stdin.read().strip().splitlines()
casos = int(linhas_entrada[0])

resultados = []

for numero_caso in range(1, casos + 1):
    quantidade = int(linhas_entrada[2 * numero_caso - 1])
    valores = list(map(int, linhas_entrada[2 * numero_caso].split()))
    
    raiz_bst = None
    for valor in valores:
        raiz_bst = inserir(raiz_bst, valor)

    pre = percurso_pre_ordem(raiz_bst)
    ino = percurso_in_ordem(raiz_bst)
    pos = percurso_pos_ordem(raiz_bst)

    resultados.append(f"Case {numero_caso}:")
    resultados.append("Pre.: " + " ".join(map(str, pre)))
    resultados.append("In..: " + " ".join(map(str, ino)))
    resultados.append("Post: " + " ".join(map(str, pos)))
    resultados.append("")  # linha em branco após cada caso

print("\n".join(resultados))
