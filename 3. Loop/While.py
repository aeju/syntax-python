# 조건문이 참일 때, 반복적으로 코드 수행

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행

# 1)
while i <= 9:
    result +=  i
    i += 1

print(result)

# 2)

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)