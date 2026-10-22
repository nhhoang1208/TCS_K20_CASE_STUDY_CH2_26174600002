tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60
print("Tổng", tong_phut, "phút tương đương:", so_gio, "giờ và", phut_con_lai, "phút.")
su_dung_lau = tong_phut > 60
print("Sử dụng lâu hơn 60 phút:", su_dung_lau)
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

#. Dự đoán và kiểm chứng hai biểu thức
#. Dự đoán: 100 + 20 * 3 = 160 (Nhân trước cộng sau)
#. Dự đoán: (100 + 20) * 3 = 360 (Cộng trong ngoặc trước nhân sau)
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)
