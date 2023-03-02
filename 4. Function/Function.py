# 함수 : 동일한 알고리즘 반복적으로 수행해야 할 때 사용
# def 함수명(매개변수)::
    # 실행할 소스코드
    # return 반환 값

def add(a, b):
    return a + b

print(add(3,7))


# return 없어도 o (함수 안에서 결과까지 출력하도록 하는 경우)
def add(a, b):
    print('함수의 결과:', a+b)

add(3,7)

# 파라미터의 변수 직접 지정해서 값 넣기
def aeju(a, b):
    print('함수의 결과:', a+b)

aeju(b = 3, a = 7)


# global : 함수 안에서 함수 밖의 변수 데이터 변경해야 하는 경우
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다 표현식 -> 함수를 매우 간단하게 작성 가능 (한 줄에 작성)
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))