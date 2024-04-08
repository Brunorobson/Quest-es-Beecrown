list = []
while True:
    x = float(input())

    if x >= 0 and x <= 10:
        list.append(x)
    else:
        print("nota invalida")

    if len(list) == 2:
        soma = sum(list)/2
        print("media = ",soma)
        break

    
        
