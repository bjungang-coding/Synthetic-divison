N = int(input())
L = map(int, input().split(" "))

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