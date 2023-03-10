# data : 집합 자료형 (집합을 처리하기 위함, 리스트 혹은 문자열(스트링)으로 만듦)
# 특징 1 : 중복 허용x
# 특징 2 : 순서 x (인덱싱 불가능)
# 특정 데이터가 이미 등장한 적이 있는지 여부 체크할 때 효과적
# set([]) or { }

# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5,6}
print(data)

# 집합 자료형 연산 : 합집합, 교집합, 차집합 (|, &, -)

a = set([1, 2, 3, 4, 5])
b = {3, 4, 5, 6, 7}

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합