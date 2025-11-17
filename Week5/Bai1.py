def remove_punctuation(text: str) -> str:
    for c in text:
        if not c.isalnum():
            if c == ' ':
                continue
            text = text.replace(c, '')
    return text


def to_lower(s: str) -> str:
    return s.lower()


def remove_stopwords(text: str, stopwords: list[str]) -> str:
    word_list = text.split()
    res = ""
    for word in word_list:
        if word not in stopwords:
            res += word
            res += " "
    return res


def pipeline(s: str, functions) -> str:
    for f in functions:
        s = f(s)
    return s


def count_words(s: str) -> dict:
    word_list = s.split()
    res = dict()
    for word in word_list:
        res[word] = res.get(word, 0) + 1
    return res

text1 = input()
print(remove_punctuation(text1))

text2 = input()
print(to_lower(text2))

text3 = input()
stopword1 = input().split(", ")
print(remove_stopwords(text3, stopword1))

text4 = input()
stop = input().split(", ")
print(pipeline(text4,  [remove_punctuation, to_lower, lambda x: remove_stopwords(x, stop)]))

text5= input()
print(count_words(text5))