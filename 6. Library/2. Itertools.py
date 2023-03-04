# itertools : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
# 코테에서 가장 유용한 클래스 : permutations, combinations
# 순열, 조합에 대한 설명 : 부록 B

# 1. permutations(순열) : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산해줌
# 클래스이므로 객체 초기화 이후, 리스트 자료형으로 변환하여 사용

# 리스트에서 3개(r=3)를 뽑아 나열하는 모든 경우를 출력

from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기

print(result)


# 2. combinations(조합) : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
# 순서에 상관없이 나열!

from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
result2 = list(combinations(data, 3)) # 3개 뽑는 조합 = a, b, c

print(result)
print(result2)

# 3. product : r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) + 원소 중복 o
# product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어줌

from  itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
# result2 = list(product(data, repeat=3)) # 3개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
# print(result2)

# 4. combinations_with_replacement : combination + 원소 중복 o

from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)