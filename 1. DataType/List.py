# 리스트 = 배열 = 테이블
# 여러 개의 데이터를 연속적으로 담아 처리
# 메서드 : append(), remove()


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4 (다섯 번째 원소에 접근)
print(a[4])

# 빈 리스트 선언 방법 <1>
a = list()
print(a)

# 빈 리스트 선언 방법 <2>
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
b = [0] * n
print(b)

# 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)

# 슬라이싱 (시작 인덱스 ~ 끝 인덱스 -1)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션 : 리스트를 초기화하는 방법 (대괄호 안에 조건문, 반복문 넣기 가능)
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# cf. 잘못된 방법
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)