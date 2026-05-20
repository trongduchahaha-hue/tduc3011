# CHƯƠNG TRÌNH QUẢN LÝ KHÁM BỆNH

current_year = 2026

name = input("Nhập tên bệnh nhân: ")

birth_year = int(input("Nhập năm sinh: "))

sick_days = int(input("Nhập số ngày bị bệnh: "))

temperature = float(input("Nhập nhiệt độ cơ thể: "))

exam_fee = float(input("Nhập chi phí khám: "))

if name == "":
    print("Lỗi: Tên không được để trống")

elif birth_year < 1900 or birth_year > current_year:
    print("Lỗi: Năm sinh không hợp lệ")

elif sick_days < 0:
    print("Lỗi: Số ngày bị bệnh không hợp lệ")

elif temperature < 30 or temperature > 45:
    print("Lỗi: Nhiệt độ không hợp lệ")

elif exam_fee <= 0:
    print("Lỗi: Chi phí khám phải lớn hơn 0")

else:

    age = current_year - birth_year

    extra_fee = exam_fee * 0.1

    total_fee = exam_fee + extra_fee
    if temperature > 38 and sick_days > 3:
        health_status = "Nguy hiểm"

    elif temperature > 38:
        health_status = "Sốt cao"

    elif temperature > 37.5:
        health_status = "Sốt nhẹ"

    else:
        health_status = "Bình thường"
        
    if health_status == "Nguy hiểm":

        if age > 60:
            priority = "Cấp cứu"

        else:
            priority = "Ưu tiên cao"

    else:
        priority = "Bình thường"

    fee_level = "Cao" if total_fee > 500000 else "Thấp"

    print("\n===== KẾT QUẢ KHÁM =====")

    print("Tên bệnh nhân:", name)

    print("Tuổi:", age)

    print("Số ngày bị bệnh:", sick_days)

    print("Nhiệt độ:", temperature)

    print("Tình trạng sức khỏe:", health_status)

    print("Mức độ ưu tiên:", priority)

    print("Chi phí khám:", exam_fee)

    print("Phụ phí:", extra_fee)

    print("Tổng chi phí:", total_fee)

    print("Mức chi phí:", fee_level)