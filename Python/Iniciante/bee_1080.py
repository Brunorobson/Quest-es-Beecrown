maior = 0
posmaior = 0

for i in range(1, 101):
    x = int(input())
    if i == 1 or x > maior:
        maior = x
        posmaior = i

print(maior)
print(posmaior)
