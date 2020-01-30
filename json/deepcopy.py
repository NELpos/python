import copy

a = [1, [1, 2, 3]]
b = copy.deepcopy(a)    # deep copy 실행
print(b)    # [1, [1, 2, 3]] 출력
b[0] = 100
b[1].append(4)
print(b)    # [100, [1, 2, 3, 4]] 출력
print(a)    # [1, [1, 2, 3]] 출력

"""
단순복제는 완전히 동일한 객체,
얕은복사(shallow copy)는 복합객체(껍데기)만 복사, 그 내용은 동일한 객체
깊은복사(deep copy)는 복합객체 복사 + 그 내용도 재귀적으로 복사
"""

