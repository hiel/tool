# 배열을 셀프로 비해 중복 요소 출력

list_a = [
    1,
    2,
    1,
]

temp = set()
dupes = set()
for e in list_a:
    if e in temp:
        dupes.add(e)
    else:
        temp.add(e)

print(dupes)
