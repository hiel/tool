# 두 배열을 비교해 한쪽에만 있는 요소 출력

list_a = [
    1,
    2,
]

list_b = [
    2,
    3,
]

print('#' * 5, 'only in list_a', '#' * 5)
for a in list_a:
    if a not in list_b:
        print(a)

print('#' * 5, 'only in list_b', '#' * 5)
for b in list_b:
    if b not in list_a:
        print(b)
