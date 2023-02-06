# 두 배열을 비교해 모든 요소가 같은지 체크

list_a = [
    1,
    2,
]

list_b = [
    2,
    1,
]

print("is equal" if sorted(list_a) == sorted(list_b) else "not equal")
