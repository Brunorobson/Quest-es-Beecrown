n = int(input())

for i in range(n):
    bonus = int(input())
    a1, d1, l1 = map(int, input().split())
    a2, d2, l2 = map(int, input().split())

    
    
    if l1%2 == 0:
        dabriel = ((a1 + d1)/2) + bonus
    else:
        dabriel = ((a1 + d1)/2)
    if l2%2 == 0:
        guarte = ((a2 + d2)/2) + bonus
    else:
        guarte = ((a2 + d2)/2)

    if dabriel > guarte:
        print('Dabriel')
    elif guarte > dabriel:
        print('Guarte')
    else:
        print('Empate')