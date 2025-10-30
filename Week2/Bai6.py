import re
from functools import reduce


def checkPrice(dish):
    price = re.findall(r"\d+", dish)
    if len(price) == 0:
        # print(dish)
        return 0
    return int(price[-1])


def enter():
    order = []
    while True:
        dish = input()
        if dish == "x":
            break
        elif dish == "skip":
            continue
        elif dish == "pass":
            pass
        else:
            if checkPrice(dish) != 0:
                order.append(dish)
    # print(order)
    return order


def solve(order):
    print(f"Số món: {len(order)}")
    total = sum([checkPrice(dish) for dish in order])
    if total <= 200000:
        print(f"Tổng số tiền phải trả: {total} VNĐ")
        return
    else:
        print(f"Tổng số tiền phải trả trước giảm giá: {total} VNĐ")
        discount = total * 0.1
        print(f"Giảm giá: {discount} VNĐ")
        total = total - discount
        print(f"Tổng số tiền phải trả: {total} VNĐ")



order = enter()
solve(order)
'''
cà phê sữa -> 25000
bánh ngọt -> 30000
pass
sinh tố -> abc
x

cà phê đá -> 30000
bánh kem -> 80000
nước ép cam -> 120000
skip
x
'''
