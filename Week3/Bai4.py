str = "An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"


def calGPA(uniqueNames, studentListTuple):
    res = []
    for name in uniqueNames:
        scores = [float(score) for n, score in studentListTuple if n == name]
        avg = sum(scores) / len(scores)
        res.append((name, avg))
    return res


def findMaxMinAgg(avgList):
    maxScore = avgList[0]
    minScore = avgList[0]
    for item in avgList:
        if item[1] > maxScore[1]:
            maxScore = item
        elif item[1] < minScore[1]:
            minScore = item
    return maxScore, minScore

def mySort(avgList):
    for i in range(len(avgList)):
        for j in range(len(avgList) - 1 - i):
            if (avgList[j][1] < avgList[j + 1][1]):
                avgList[j], avgList[j + 1] = avgList[j + 1], avgList[j]
    return avgList

noSpace = str.replace(" ", "")
studentList = noSpace.split(",")
# print(studentList)
studentListTuple = [tuple(item.split(":")) for item in studentList]
# print(studentListTuple)

uniqueNames = []
for name,_ in studentListTuple:
    if name not in uniqueNames:
        uniqueNames.append(name)
# print(uniqueNames)

avgList = calGPA(uniqueNames, studentListTuple)
for s in avgList:
    print(f"{s[0]}: {s[1]}")
maxStudent, minStudent = findMaxMinAgg(avgList)
print(f"Sinh viên cao nhất: {maxStudent[0]} - {maxStudent[1]}")
print(f"Sinh viên thấp nhất: {minStudent[0]} - {minStudent[1]}")

sortedList = mySort(avgList)
print(f"Sắp xếp: {sortedList}")
