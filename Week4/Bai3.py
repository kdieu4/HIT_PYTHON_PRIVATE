# coded_str = input()
#
# res = ""
# i = 0
# while i < len(coded_str):
#     if coded_str[i].isalpha():
#         res += coded_str[i]
#         i += 1
#     else:
#         break
#
# # print(res)
# size = len(res)
# for i in range(size, len(coded_str)):
#     # if coded_str[i].isalpha():
#     #     pass
#     #     # res += coded_str[i]
#     if coded_str[i].isdigit():
#         # print(coded_str[i])
#         j = i + 2
#         temp = ""
#         while coded_str[j].isalpha():
#             temp += coded_str[j]
#             j += 1
#
#         res += (int(coded_str[i])) * temp
#
#
# i = len(res)
# while i < len(coded_str):
#     if coded_str[i].isalpha():
#         res += coded_str[i]
#     i += 1
# print(res)

coded_str = input()

res = ""
i = 0
while i < len(coded_str):
    if coded_str[i].isalpha():
        res += coded_str[i]
        i += 1
    else:
        break

# print(res)
size = len(res)
for i in range(size, len(coded_str)):
    # if coded_str[i].isalpha():
    #     pass
    #     # res += coded_str[i]
    if coded_str[i].isdigit():
        # print(coded_str[i])
        j = i + 2
        temp = ""
        while coded_str[j].isalpha():
            temp += coded_str[j]
            j += 1

        res += (int(coded_str[i])) * temp

i = len(res)
while i < len(coded_str):
    if coded_str[i].isalpha():
        res += coded_str[i]
    i += 1
print(res)