numbers = [2, 3, 2, -4, 3, 5]

# 1. Loại bỏ các số trùng lặp nhưng vẫn giữ nguyên thứ tự xuất hiện
uniqueNumbers = []
for number in numbers:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)
print("1. Sau khi loại bỏ trùng: ", uniqueNumbers)

# 2. Tạo danh sách mới:
newList = [x ** 2 if x % 2 == 0 else x ** 3 for x in uniqueNumbers]
print("2. List mới: ", newList)

# 3. Tính trung bình cộng
evenIndexNumber = uniqueNumbers[::2]
average = sum(evenIndexNumber) / len(evenIndexNumber)
print("3. Trung bình vị trí chẵn: ", average)


# 4. Sắp xếp danh sách theo giá trị tuyệt đối tăng dần
def mySort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if abs(numbers[j]) > abs(numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


sortedByAbs = mySort(uniqueNumbers.copy())
print("4. Sắp xếp theo abs: ", sortedByAbs)
