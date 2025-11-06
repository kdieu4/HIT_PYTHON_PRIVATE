data = input().split()

# 5 1 3 5 2 3 4 1

# 1. Chuyển chuỗi thành list số nguyên.
listInt = list(map(int, data))

# 2.  đoạn con liên tiếp dài nhất (subarray) mà không có phần tử nào lặp lại.
dp = []  # dp[i] độ dài đoạn con liên tiếp dài nhất không có đoạn con nào lặp lại

for i in range(len(listInt)):
    dp.append(1)

res = []
# res.extend(listInt[0])

for i in range(0, len(listInt)):
    if i == 0:
        res.append(listInt[i])
    elif listInt[i] != listInt[i - 1] and listInt[i] in res:
        # print("SOS")
        res.clear()
        res.append(listInt[i])
    elif listInt[i] != listInt[i - 1] and listInt[i] not in res:
        res.append(listInt[i])
        dp[i] = dp[i - 1] + 1

res = tuple(res)
print("Đoạn con dài nhất:", res)
print("Độ dài:", max(dp))
