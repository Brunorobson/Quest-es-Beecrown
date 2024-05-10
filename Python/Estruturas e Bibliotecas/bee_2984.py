def contar_assuntos_pendentes(expressao):
    assuntos_pendentes = 0
    aberturas_pendentes = 0
    
    for char in expressao:
        if char == '(':   # Parêntese de abertura
            aberturas_pendentes += 1
        elif char == ')':   # Parêntese de fechamento
            if aberturas_pendentes > 0:  # Se houver parênteses de abertura pendentes
                aberturas_pendentes -= 1  # Fecha um parêntese de abertura
            else:  # Se não houver parênteses de abertura pendentes, significa que este parêntese de fechamento não tem par
                assuntos_pendentes += 1
    
    return aberturas_pendentes

def verificar_assuntos_pendentes(expressao):
    assuntos_pendentes = contar_assuntos_pendentes(expressao)
    
    if assuntos_pendentes > 0:
        print("Ainda temos", assuntos_pendentes, "assunto(s) pendente(s)!")
    else:
        print("Partiu RU!")


def main():
    expressao = input()
    verificar_assuntos_pendentes(expressao)

if __name__ == "__main__":
    main()
