
while True:
    t = int(input())
    alimento = 0
    soma = 0
    if t == 0:
        break

    for i in range(t):
        n = list(map(str,input().split()))
        quantidade = int(n[0])
        if n[1] == "suco":
            alimento = 120
        elif n[1] == "morango":
            alimento = 85
        elif n[1] == "mamao":
            alimento = 85
        elif n[1] == "goiaba":
            alimento = 70
        elif n[1] == "manga":
            alimento = 56
        elif n[1] == "laranja":
            alimento = 50
        elif n[1] == "brocolis":
            alimento = 34

        soma = soma + (quantidade * alimento)

    if soma <= 110:
        print(f"Mais {110 - soma} mg")
    elif soma >= 130:
        print(f"Menos {soma - 130} mg")
    elif soma > 110 and soma < 130: 
        print(f"{soma} mg")
