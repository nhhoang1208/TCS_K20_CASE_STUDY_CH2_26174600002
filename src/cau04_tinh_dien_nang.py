cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--- LẦN 1: SO_PHUT = 90 ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

#. Dự đoán kết quả trước khi chạy 
#. Điện năng: 0.375 kWh (Kiểu float)
#. Chi phí: 1125.0 VND (Kiểu float)

print("------------------------------------")

so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--- LẦN 2: SO_PHUT = 60 ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))
#. So sánh: Khi giảm thời gian từ 90 phút xuống 60 phút
#. Điện năng tiêu thụ giảm từ 0.375 kWh xuống 0.25 kWh.
#. Chi phí điện giảm từ 1125.0 VND xuống 750.0 VND.