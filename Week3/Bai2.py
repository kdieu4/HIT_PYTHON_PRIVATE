# s = input("Nhập chuỗi: ")
s = "Able , was I saw Elba!"


def myStandardize(str):
    res = ""
    for ch in str:
        if ch.isalpha() or ch == " ":
            res += ch
    return res


def countVowelConsonant(str):
    str = str.replace(" ", "")
    vowels = "ueoai"
    cntVowel = sum(1 for char in str if char in vowels)
    cntConsonant = sum(1 for char in str if char not in vowels and char not in vowels)
    return cntVowel, cntConsonant


def reverseEachWord(str):
    res = myStandardize(str).split(" ")
    res = [word[::-1] for word in res]
    return res


def isPalindrome(str):
    # print(str)
    noSpace = str.replace(" ", "").lower()
    # print(noSpace)
    return noSpace == noSpace[::-1]


standardizedString = myStandardize(s).lower()
print("Chuẩn hóa:", standardizedString)

cntVowel, cntConsonant = countVowelConsonant(standardizedString)
print("Nguyên âm:", cntVowel, "Phụ âm:", cntConsonant)

reversedEachWord = reverseEachWord(s)
print(f"Đảo từng từ: {reversedEachWord}")

print(f"Palindrome: {isPalindrome(standardizedString)}")
