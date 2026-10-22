ma_may_inp = input("Mã máy: ")
print("Mã máy vừa nhập:", ma_may_inp, "| Kiểu:", type(ma_may_inp))

cong_suat_inp = input("Công suất (W): ")
print("Công suất vừa nhập:", cong_suat_inp, "| Kiểu:", type(cong_suat_inp))

so_phut_inp = input("Số phút sử dụng: ")
print("Số phút vừa nhập:", so_phut_inp, "| Kiểu:", type(so_phut_inp))

don_gia_inp = input("Đơn giá (VND/kWh): ")
print("Đơn giá vừa nhập:", don_gia_inp, "| Kiểu:", type(don_gia_inp))

print("----------------------------------")

ma_may = ma_may_inp
cong_suat_w = float(cong_suat_inp)
so_phut = int(so_phut_inp)
don_gia_kwh = float(don_gia_inp)

print("Kiểu dữ liệu sau khi chuyển đổi:")
print("Mã máy:", type(ma_may))
print("Công suất:", type(cong_suat_w))
print("Số phút:", type(so_phut))
print("Đơn giá:", type(don_gia_kwh))

print("----------------------------------")

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- KẾT QUẢ TÍNH TOÁN ---")
print("Mã máy:", ma_may)
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí điện (VND):", chi_phi)