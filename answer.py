N = int(input())
L = map(int, input().split())
X = int(input())

index = 0
result = []

for l in L:
    if index == 0:
        result.append(l)
    else:
        result.append(result[index-1]*X + l)
    index += 1

remainder = result.pop(-1)
print(result)
print(remainder)
