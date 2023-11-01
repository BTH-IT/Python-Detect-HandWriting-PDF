import cv2

# Đọc hình ảnh bằng OpenCV
image = cv2.imread("Images/English.jpg")

# Thiết lập tỷ lệ tăng kích thước
scale_factor = 2  # Ví dụ: tăng kích thước gấp đôi

# Tăng kích thước hình ảnh
new_width = int(image.shape[1] * scale_factor)
new_height = int(image.shape[0] * scale_factor * 2)
resized_image = cv2.resize(image, (new_width, new_height))

# Lưu hình ảnh đã được xử lý
cv2.imwrite("resized_image.png", resized_image)

# Hiển thị hình ảnh đã được xử lý
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()