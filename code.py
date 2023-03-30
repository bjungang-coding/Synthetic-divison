import re

term_count = int(input("계산하려는 식의 최대 차수 : "))
degree_list = [int(input(f"차수가 {term_count - _}인 항의 계수 : ")) for _ in range(term_count)]
degree_list.append(int(input("상수항 : ")))

def find_x(equation):
    pattern = r"\+?\s*(\d+)\s*\)"
    match = re.search(pattern, equation)
    if match:
        if "+" in equation:
            return -(int(match.group(1)))
        else:
            return (int(match.group(1)))


factor = find_x(input("나눌려는 식 : "))
print(factor)
index = 0
result = []
for i in degree_list:
    if index == 0:
        result.append(i)
    else:
        result.append(result[index-1] * factor + i)
    index += 1

print(result)
