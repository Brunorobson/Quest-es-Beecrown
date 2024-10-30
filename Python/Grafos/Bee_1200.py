class TreeNode:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.val = chave

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = TreeNode(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if chave < no.val:
            if no.esquerda is None:
                no.esquerda = TreeNode(chave)
            else:
                self._inserir_recursivo(no.esquerda, chave)
        else:
            if no.direita is None:
                no.direita = TreeNode(chave)
            else:
                self._inserir_recursivo(no.direita, chave)

    def inorder(self):
        return self._inorder_recursivo(self.raiz)

    def _inorder_recursivo(self, no):
        if no is None:
            return []
        return self._inorder_recursivo(no.esquerda) + [no.val] + self._inorder_recursivo(no.direita)

    def preorder(self):
        return self._preorder_recursivo(self.raiz)

    def _preorder_recursivo(self, no):
        if no is None:
            return []
        return [no.val] + self._preorder_recursivo(no.esquerda) + self._preorder_recursivo(no.direita)

    def postorder(self):
        return self._postorder_recursivo(self.raiz)

    def _postorder_recursivo(self, no):
        if no is None:
            return []
        return self._postorder_recursivo(no.esquerda) + self._postorder_recursivo(no.direita) + [no.val]

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return False
        if no.val == chave:
            return True
        elif chave < no.val:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

import sys

arvore = ArvoreBinariaBusca()

for linha in sys.stdin:
    linha = linha.strip()
    comando = linha.split()
    
    if comando[0] == 'I':
        arvore.inserir(comando[1])
    elif comando[0] == 'INFIXA':
        print(" ".join(arvore.inorder()))
    elif comando[0] == 'PREFIXA':
        print(" ".join(arvore.preorder()))
    elif comando[0] == 'POSFIXA':
        print(" ".join(arvore.postorder()))
    elif comando[0] == 'P':
        elemento = comando[1]
        if arvore.buscar(elemento):
            print(f"{elemento} existe")
        else:
            print(f"{elemento} nao existe")
