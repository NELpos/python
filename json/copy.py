#copy

a = [1, 2, 3, 4]
b = a     # shallow copy
print(b)    # [1, 2, 3, 4]
b[2] = 100   # b의 item 변경
print(b)    # [1, 2, 100, 4]
print(a)    # [1, 2, 100, 4], a의 item도 수정됨!!


