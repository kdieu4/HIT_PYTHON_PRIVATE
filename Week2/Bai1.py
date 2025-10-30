def solve1(x, n):
    ans = 1.0
    b = 1
    for i in range(1, n + 1):
        a = x ** i
        b = i * b
        ans = ans + a / b
    return round(ans, 3)


def solve2(n):
    ans = 1.0
    b = 1
    for i in range(1, n + 1):
        b = i * b
        ans = ans + 1 / b
    return round(ans, 3)


if __name__ == '__main__':
    x = float(input("Nhap gia tri x: "))
    n = int(input("Nhap gia tri n: "))
    print(f"Gia tri xap xi cua e^x la {solve1(x, n)}")
    print(f"Gia tri S la {solve2(n)}")
