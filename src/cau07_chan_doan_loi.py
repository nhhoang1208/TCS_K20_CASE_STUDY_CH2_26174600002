ma_may = input("Mã máy: ")
# Sửa lỗi 1: Ép kiểu float cho cong_suat_w
cong_suat_w = float(input("Công suất W: "))
so_phut = int(input("Số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
# Sửa lỗi 2: Sửa dien_nang thành dien_nang_kwh
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# PHẦN COMMENT MÔ TẢ CÁC LỖI ĐÃ PHÁT HIỆN
# Lỗi 1:
# - Tệp: src/cau07_chan_doan_loi.py | Dòng: 5
# - Loại lỗi: TypeError (can't multiply sequence by non-int of type 'float')
# - Nguyên nhân: Biến cong_suat_w chưa ép kiểu nên mang kiểu str, không thể thực hiện phép toán số học.
# - Cách khắc phục: Ép kiểu biến cong_suat_w thành float bằng hàm float().
# Lỗi 2:
# - Tệp: src/cau07_chan_doan_loi.py | Dòng: 7
# - Loại lỗi: NameError (name 'dien_nang' is not defined)
# - Nguyên nhân: Viết sai tên biến trong hàm print(), biến đúng được tạo ở trên là dien_nang_kwh.
# - Cách khắc phục: Đổi tên biến dien_nang trong f-string thành dien_nang_kwh.