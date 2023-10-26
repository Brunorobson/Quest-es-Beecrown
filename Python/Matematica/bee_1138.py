def contar_digitos_entre_a_e_b(a, b):
    frequencia_digitos = [0] * 10
    posicao = 1

    while a <= b:
        while b % 10 != 9 and a <= b:
            for i in str(b):
                frequencia_digitos[int(i)] += posicao
            b -= 1

        while a % 10 != 0 and a <= b:
            for i in str(a):
                frequencia_digitos[int(i)] += posicao
            a += 1

        if a > b:
            break

        a //= 10
        b //= 10

        for i in range(10):
            frequencia_digitos[i] += (b - a + 1) * posicao

        posicao *= 10

    return frequencia_digitos

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    frequencia = contar_digitos_entre_a_e_b(a, b)
    print(*frequencia)
