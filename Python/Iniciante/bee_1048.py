abc = float(input())

if abc >= 0 and abc<=400:
    soma = (abc * 15) / 100
    valor = soma + abc
    print("Novo salario: %0.2f" %valor)
    print("Reajuste ganho: %0.2f" %soma)
    print("Em percentual: 15 %")
elif abc > 400 and abc<=800:
    soma = (abc * 12)/100
    valor = soma + abc
    print("Novo salario: %0.2f" %valor)
    print("Reajuste ganho: %0.2f" %soma)
    print("Em percentual: 12 %")
elif abc > 800 and abc<=1200:
    soma = (abc * 10)/100
    valor = soma + abc
    print("Novo salario: %0.2f" %valor)
    print("Reajuste ganho: %0.2f" %soma)
    print("Em percentual: 10 %")
elif abc > 1200 and abc<=2000:
    soma = (abc * 7)/100
    valor = soma + abc
    print("Novo salario: %0.2f" %valor)
    print("Reajuste ganho: %0.2f" %soma)
    print("Em percentual: 7 %")
elif abc > 2000:
    soma = (abc * 4)/100
    valor = soma + abc
    print("Novo salario: %0.2f" %valor)
    print("Reajuste ganho: %0.2f" %soma)
    print("Em percentual: 4 %")