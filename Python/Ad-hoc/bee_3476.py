S, B, C = map(int, input().split())

tempo_medio = (S * B * C) / (S * B + B * C + C * S)

print('{:.3f}'.format(tempo_medio))