from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print("Thời điểm hiện tại (datetime):", thoi_diem)
print("Kiểu của thoi_diem:", type(thoi_diem))
print("Thời điểm hiện tại (chuỗi str):", thoi_diem_text)
print("Kiểu của thoi_diem_text:", type(thoi_diem_text))
print("-------------------------------")

# Dự đoán kết quả phép trừ trước khi chạy:
# - bat_dau = 13:15 ngày 14/10/2026
# - ket_thuc = 15:05 ngày 14/10/2026
# - Dự đoán thoi_luong = 1 giờ 50 phút (1:50:00)
# - Kiểu dữ liệu dự đoán: <class 'datetime.timedelta'>

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print("Thời lượng:", thoi_luong)
print("Kiểu của thoi_luong:", type(thoi_luong))

# GIẢI THÍCH SỰ KHÁC NHAU:
# - datetime: Đối tượng lưu trữ mốc thời gian cụ thể (Năm, Tháng, Ngày, Giờ, Phút, Giây).
# - str: Chuỗi văn bản hiển thị mốc thời gian đã qua định dạng strftime để in ra/hiển thị.
# - timedelta: Khoảng thời gian chênh lệch (thời lượng) thu được từ phép tính toán giữa 2 mốc datetime.