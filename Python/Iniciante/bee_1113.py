while True:
    x, y = list(map(int,input().split()))

    if x > y:
        print("Decrescente")
    elif y > x:
        print("Crescente")
    elif x == x:
        break