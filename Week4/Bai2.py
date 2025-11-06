originText = input()

# print(originText)
normalText = originText.lower()
print(normalText)
res = {}
for ch in normalText:
    if ch not in res:
        res.update({ch: 1})
    else:
        res[ch] += 1

print(res)
