# 한 배열의 중복 요소 건수 출력

list_a = [
    1,
    2,
    1,
    2,
    1,
    3,
    1,
]

dupes = dict()
for e in list_a:
    if e not in dupes:
        dupes[e] = 0
    dupes[e] += 1


for k, v in sorted(dupes.items(), key=lambda e: e[1], reverse=True):
    print(f'value={k} count={v}')
