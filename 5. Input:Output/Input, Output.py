# 데이터 입력 : input() <- 문자열
# 입력받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장 : list(map(int, input().split()))


# 1. 입력을 위한 전형적인 소스코드
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 2. 공백을 기준으로 구부하여 적은 수의 데이터 입력
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 3. 입력 최대한 빠르게 받아야 하는 경우 (정렬, 이진 탐색, 최단 경로 문제 <- 1000만 개의 넘는 라인, 입력 받는 것만으로도 시간 초과)
# -> sys 라이브러리에 정의되어 있는 sys.stdin.readline()
# import sys
# sys.stdin.readline().rstrip()

# readline() 사용 소스코드
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

# 출력 : print

# 출력할 변수들
a = 1
b = 2

print(a, b)

# 출력 줄 바꿈
print(a)
print(b)

# 문자열, 수 함께 출력해야 되는 경우 -> + 사용하면 오류
# 1st 방법 : str() 함수 이용하여 출력하고자 하는 변수 데이터 문자열로 바꾸기
# 2nd 방법 : 각 자료형을 , 기준으로 구분하여 출력 (변수 값 사이 의도치 않은 공백!)

# 출력할 변수들
answer = 7

print("정답은 " + str(answer) + "입니다.")
# 오류 : print("정답은 " + answer + "입니다.")

print("정답은", str(answer), "입니다.")

# f-string (python 3.6 이상) -> 중괄호 안에 변수 넣음으로써, 자료형 변환 없이도 문자열 정수 함께 넣을 수 있음
print(f"정답은 {answer}입니다.")