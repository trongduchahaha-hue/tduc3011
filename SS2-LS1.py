heart_rate = int(input("Nhập nhịp tim bệnh nhân: "))

if heart_rate > 120:
    print("RED - Nguy kịch")

elif heart_rate > 100:
    print("YELLOW - Cần theo dõi")

elif heart_rate < 60:
    print("BLUE - Nhịp tim chậm")

else:
    print("GREEN - Ổn định")
 


