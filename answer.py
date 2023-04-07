N = int(input())
L = [int(input()) for i in N + 1]

index = 0
result = []

for l in L:
    if index == 0:
        result.append(l)
    else:
        result.append(result[index-1] + l)
    index += 1

remainder = result.pop(-1)
print(x for x in result)
print(remainder)
