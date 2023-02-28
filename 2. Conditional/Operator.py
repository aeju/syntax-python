# 비교 연산자 : ==, !=, >, <, >=, <=

score = 85


# 1
if score >= 80:
    pass # 나중에 작성할 소스 코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 2
if score >= 80: result = "Succes"
else: result = "Fail"
print(result)

# 3 조건문 표현식 (if ~else문 한 줄에 작성 가능)
result = "Success" if score >= 80 else "Fail"
print(result)

# 4
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [ ]
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 4-2 (더 간단하게)
result = [i for i in a if i not in remove_set]

print(result)

# 논리 연산자 : and, or, not

# 기타 연산자 : in, not in (자료형 안에 어떠한 값이 존재하는지 확인)
