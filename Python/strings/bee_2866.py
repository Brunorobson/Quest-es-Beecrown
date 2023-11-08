n = int(input())
while n > 0:
    n-=1
    nome = input()
    nova = (letra for letra in nome if letra.islower())
    nova = "".join(nova[::-1])
    print(nova)
    


