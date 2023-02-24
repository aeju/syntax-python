# Dictionary(사전 자료형) : key, value 쌍을 데이터로 가지는 자료형
# 키 - 값 -> 리스트보다 빠르게 동작
# 키 : 변경 불가능한 데이터를 키로 사용
# 예시 : 사전 (사과 - apple) / 사과 : apple

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
