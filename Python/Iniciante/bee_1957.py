hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
list = []
n = int(input())
valor = n
while n > 0:
    list.append(hex[n%16])
    n = n // 16
for i in range(len(list)-1,-1,-1):
    print(list[i],end="")
print("")

