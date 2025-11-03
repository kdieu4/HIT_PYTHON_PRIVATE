# Bài 1 – Danh sách điểm sinh viên (List)
# Yêu cầu: Viết chương trình quản lý danh sách điểm của sinh viên:

# Nhập danh sách điểm từ bàn phím (các số cách nhau bởi dấu cách).
# points = input("Nhập danh sách điểm: ").split()
# print(points)

points = ['4', '2', '3', '8', '9']

# Loại bỏ điểm nhỏ hơn 5.
points_greater_5 = []
for point in points:
    if int(point) >= 5:
        points_greater_5.append(point)
print("Danh sách sau khi loại bỏ điểm nhỏ hơn 5", points_greater_5)

# Sắp xếp danh sách còn lại theo thứ tự giảm dần.
points_greater_5.sort(reverse = 'True')
print("Danh sách còn lại theo thứ tự giảm dần", points_greater_5)

# In ra danh sách điểm hợp lệ và điểm cao nhất, thấp nhất.
print("Danh sách hợp lệ ", points_greater_5)
print("Điểm cao nhất là: ", max(points_greater_5))
print("Điểm cao nhất là: ", points_greater_5[0])
print("Điểm thấp nhất là: ", min(points_greater_5))
