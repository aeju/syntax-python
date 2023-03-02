# for 변수 in 리스트(튜플, 문자열...):
#   실행할 소스코드
# range(시작 값, 끝 값 + 1)
# range(n) = (0, n+1) <- 모든 원소를 첫 번째 인덱스부터 방문해야 할 때 사용(= 리스트의 인덱스는 0부터 출발)

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i +1, "번 학생은 합격입니다.")

# continue : 반복문의 처음으로 돌아감 (= 점수 높아도 합격x)
black_list = {2,4}

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# 2중 반복문 (2단 ~ 9단)
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()