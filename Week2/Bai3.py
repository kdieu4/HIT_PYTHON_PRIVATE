n = int(input())

res_list = []
for i in range(n):
    name = input()
    tx1 = int(input())
    tx2 = int(input())

    stt = i + 1
    total = tx1 + tx2
    if total >= 200:
        level = "Xuất sắc"
    elif total >= 150:
        level = "Giỏi"
    elif total >= 100:
        level = "Khá"
    else:
        level = "Yếu"
    res_line = f"{stt} {name} {total} {level}"
    res_list.append(res_line)

for i in res_list:
    print(i)
