ini, fin = list(map(int,input().split()))

if fin <= ini:
    print("O JOGO DUROU",24 -(ini - fin),"HORA(S)")
else:
    print("O JOGO DUROU",(fin - ini),"HORA(S)")