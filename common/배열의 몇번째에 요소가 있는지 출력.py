# 배열의 몇번째에 요소가 있는지 출력

element = 2

list_a = [
    1,
    2,
]

try:
    print("#" * 5, "start with 1", "#" * 5)
    print(list_a.index(element) + 1)
except ValueError:
    print("not exists")
