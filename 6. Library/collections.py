# collections 라이브러리 : 자료구조 제공(deaue, Counter)

# deque : 큐 구현
# 인덱싱, 슬라이싱 x
# 연속적으로 나열된 데이터의 시작 부분 Or 끝부분에 데이터 삽입,삭제할 때 효과적
# cf. 리스트 : append(), pop() <- '가장 뒤쪽 원소' 기준으로 수행 (=앞쪽에 있는 원소 처리할 때 데이터 개수에 따라 많은 시간 소요)
# <원소 제거>
# 첫 번째 원소 : popleft()
# 마지막 원소 : pop()
# <원소 삽입>
# 첫 번째 인덱스 : appendleft(x)
# 마지막 인덱스 : append(x)

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])로 출력돼서
print(list(data)) # 리스트 자료형으로 변환

# Counter : 등장 횟수 세는 기능 (iterable 객체 주어졌을 때)
from  collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력, 3
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환 ...오