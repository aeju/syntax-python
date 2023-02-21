#정수형
print("정수형 : 양의 정수, 음의 정수, 0")
# 양의 정수
a = 1000
print(a)

#음의 정수
a = -7
print(a)

a = 0
print(a)

#실수형
print("실수형")

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

a = 5.
print(a)

a = -.7
print(a)

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# round() : 소수점 특정 자릿수에서 반올림하는 함수

#print("round(a, 4) : " + round(a, 4))
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)