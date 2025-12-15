import numpy as np

# python_list = [1, 2, 3, 4, 5]
# numpy_array = np.array([1, 2, 3, 4, 5])
#
# print("Python list:", python_list)
# print("NumPy array:", numpy_array)
# print("Type của numpy array:", type(numpy_array))

import numpy as np
# Tạo mảng 1 chiều
arr1d = np.array([1, 2, 3, 4, 5])
print("Mảng 1D:", arr1d)
print("Số chiều (ndim):", arr1d.ndim)
print("Kích thước (shape):", arr1d.shape)
print("Số phần tử (size):", arr1d.size)
print("Kiểu dữ liệu (dtype):", arr1d.dtype)
print("Kích thước mỗi phần tử (itemsize):", arr1d.itemsize, "bytes")

# Tạo mảng 2 chiều
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMảng 2D:")
print(arr2d)
print("Shape:", arr2d.shape)  # (2, 3) - 2 hàng, 3 cột
print("Ndims:", arr2d.ndim)

# Tạo mảng 3 chiều
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nMảng 3D:")
print(arr3d)
print("\nMảng 3D shape:", arr3d.shape)  # (2, 2, 2)


# ==== 3. Tao mang ======
# Tạo mảng với giá trị đặc biệt
zeros_arr = np.zeros((3, 4))  # Ma trận 3x4 toàn số 0
print("Zeros array:\n", zeros_arr)

ones_arr = np.ones((2, 3), dtype=np.int32)  # Ma trận 2x3 toàn số 1
print("\nOnes array:\n", ones_arr)

full_arr = np.full((2, 2), 7)  # Ma trận 2x2 toàn số 7
print("\nFull array:\n", full_arr)

# Tạo dãy số
range_arr = np.arange(0, 10, 2)  # Tương tự range(0, 10, 2)
print("\nArrange array:", range_arr)

linspace_arr = np.linspace(0, 1, 5)  # 5 số từ 0 đến 1 cách đều
print("Linspace array:", linspace_arr)

# Ma trận đơn vị
identity_matrix = np.eye(3)
print("\nMa trận đơn vị 3x3:\n", identity_matrix)

# Mảng ngẫu nhiên
random_arr = np.random.rand(2, 3)  # Số ngẫu nhiên từ [0, 1)
print("\nRandom array:\n", random_arr)

normal_arr = np.random.randn(3, 3)  # Phân phối chuẩn (mean=0, std=1)
print("\nNormal distribution array:\n", normal_arr)

int_random = np.random.randint(1, 100, (3, 4))  # Số nguyên từ 1-99
print("\nRandom integers:\n", int_random)

# 1. Lý thuyết
# 2. Các phép tính
# 3. Bài tập