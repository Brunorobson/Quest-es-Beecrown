N, C, T = map(int, input().split())
pipocas = list(map(int, input().split()))

inicio, fim = max(pipocas), sum(pipocas)

print(inicio, fim)
