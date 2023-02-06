# 두 db row를 비교해 값이 다른 컬럼 출력
# row delimiter : \n
# column delimiter : \t

rows = [
    # "PRODUCT_ID	PRODUCT_NAME",
    # "1	'상품명1'",
    # "2	'상품명2'",
]

columns = rows[0].split('\t')
cells_a = rows[1].split('\t')
cells_b = rows[2].split('\t')

for i, cell in enumerate(cells_a):
    if cells_b[i] != cell:
        print(columns[i], cells_a[i], cells_b[i])
