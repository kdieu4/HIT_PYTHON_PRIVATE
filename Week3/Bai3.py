paragraph = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
             "sed do eiusmod tempor incididunt ut labore et dolore magna "
             "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
             "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
             "Duis aute irure dolor in reprehenderit in voluptate velit "
             "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
             "occaecat cupidatat non proident, sunt in culpa qui officia "
             "deserunt mollit anim id est laborum.")

# B1: Chuẩn hóa
paragraph = paragraph.lower()
for c in ".,!?;:":
    paragraph = paragraph.replace(c, '')
splitParagraph = paragraph.split(" ")
print(f"Danh sách sau khi tách từ: {splitParagraph}")

# B2: Tạo list từ duy nhất theo thứ tự
uniqueWordParagraph = []
for word in splitParagraph:
    if word not in uniqueWordParagraph:
        uniqueWordParagraph.append(word)
print(f"Danh sách các từ duy nhất: {uniqueWordParagraph}")

# B3: Đếm số lần xuất hiện
countWord = []
for word in uniqueWordParagraph:
    countWord.append((word, splitParagraph.count(word)))

print(f"Số lần xuất hiện từng từ\n {countWord}")

# B4: Tìm từ tần suất cao nhất, dài nhất, tổng ký tự
# print(type(countWord))
# print(type(countWord[0]))
maxLength = countWord[0]
maxFreq = countWord[0]

for item in countWord:
    if len(item[0]) > len(maxLength[0]):
        maxLength = item
    if maxFreq[1] < item[1]:
        maxFreq = item

print(f"Từ có tần xuất xuất hiện cao nhất: {maxFreq[0]} - {maxFreq[1]}")
print(f"Từ dài nhất: {maxLength[0]} - {len(maxLength[0])}")

totalChars = sum(len(word) for word in splitParagraph)
print(f"Tổng số ký tự: {totalChars}")


# B5: Sắp xếp giảm dần theo độ dài (không dùng sort)
def mySort(listToSort):
    for i in range(len(listToSort)):
        for j in range(len(listToSort) - i - 1):
            if len(listToSort[j]) < len(listToSort[j + 1]):
                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
    return listToSort


sortedList = mySort(uniqueWordParagraph)
print(f"Sắp xếp: \n{sortedList}")
