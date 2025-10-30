def solve(n):
    ans = 0
    for i in range(2, n):
        # print(i)
        if n % i == 0 and i % 2 == 1:
            ans = ans + 1
    return ans

if __name__ == "__main__":
    n = int(input("Nhap so n: "))
    print(f"So uoc le trong khoang tu 1 den n: {solve(n)}")
    # solve(n)