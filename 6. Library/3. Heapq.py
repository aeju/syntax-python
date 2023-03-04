# heapq 라이브러리 : heap 기능 (PriorityQueue 라이브러리보다 빠름)
# 다익스트라 최단 경로 알고리즘 -> 우선 순위 큐 기능 구현할 때

# 파이썬의 힙 : 최소 힙으로 구성 -> 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬 완료
# 보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은' 원소이기 때문

# heapq.heappush() 메서드 : 힙에 원소 삽입
# heapq.heappop() : 힙에서 원소를 꺼낼 때

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬, 최대 힙 제공 x
# heapq 라이브러리 이용하여 최대 힙 구현 : 원소의 부호를 임시로 변경하는 방식
# (힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꿈)

# 최대 힙을 구현하여 오름차순 힙 정렬을 구현하는 예시

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)