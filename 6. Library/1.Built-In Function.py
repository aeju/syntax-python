# 표준 라이브러리 : 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
# C++ : C++ STL (Standard Template Library), Python : 파이썬 표준 라이브러리
# https://docs.python.org/ko/3/library/index.html
# 코테 -> 6가지

# 1. 내장 함수 : 기본 내장 라이브러리 -> 입출력(print, input), 정렬(sorted)
# 2. itertools : 반복되는 형태의 데이터를 처리하는 기능 제공 -> 순열, 조합
# 3. heapq : 힙 기능 -> 우선순위 큐 기능 구현
# 4. bisect : 이진 탐색 기능 제공
# 5. collections : 덱, 카운터 등 유용한 자료구조 포함
# 6. math : 필수적인 수학적 기능 제공 -> 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 메서드 + 파이 상수


# 내장 함수 : import 명령어 없이 바로 사용 가능
# input(), print(), sum(), min(), max(), eval(), sorted()

# (3) sum() : iterable 객체(반복 가능한 객체 -> 리스트, 사전 자료형, 튜플 자료형) 입력 -> 모든 원소의 합
result = sum([1, 2, 3, 4, 5])
print(result)

# min() : 파라미터 중 가장 작은 값 반환
result = min(7, 3, 5, 2)
print(result)

# max() : 가장 큰 값 반환
result = max(7, 3, 5, 2)
print(result)

# eval() : 수학 수식 문자열 형식으로 들어오면, 해당 수식 계산한 결과 반환
result = eval("(3 + 5) * 7")
print(result)

# sorted() : 정렬된 결과 반환
# key 속성 -> 정렬 기준 명시 가능
# reverse 속성 : 정렬된 결과 리스트 뒤집을지 여부 설정 가능

# 오름차순으로 정렬
result = sorted([9, 1, 8, 5, 4])
print(result)

# 내림차순으로 정렬
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# key 속성 -> 튜플의 두 번째 원소를 기준으로 내림차순으로 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True)
print(result)