data = input()

# TV, Laptop, Phone, TV, Tablet, Laptop, Camera

# 1. Chuyển chuỗi thành list.
listData = data.split(", ")

# 2. Loại bỏ trùng lặp bằng set, sau đó chuyển lại thành tuple.
# In ra tuple (Hiển thị danh sách hàng hoá duy nhất)
setData = set(listData)
tupleData = tuple(setData)
print("Kho hàng (tuple):", tupleData)

# 3. Đếm số loại hàng hoá (len() tuple) và in ra số loại hàng hóa
print("Tổng số loại hàng: ", len(tupleData))

# 4. Có 3 sản phẩm bán chạy là : {"Phone", "Laptop", "Smartwatch"}.
bestSeller = {"Phone", "Laptop", "Smartwatch"}

# 5. In ra danh sách loại sản phẩm có trong kho và bán chạy (intersection).
bestSellerInData = set()
for item in tupleData:
    if item in bestSeller:
        bestSellerInData.add(item)
print ("Sản phẩm bán chạy trong kho: ")
# print(bestSellerInData)

print(bestSeller.intersection(setData))

# 6. In ra loại sản phẩm chỉ có trong kho nhưng không bán chạy (difference).
print("Sản phẩm không nằm trong danh sách bán chạy: ")
print(setData.difference(bestSeller))
# # print(data)
# for item in listData:
#     print(item)
