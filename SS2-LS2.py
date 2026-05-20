donor_age = int(input("Nhập tuổi: "))
donor_weight = float(input("Nhập cân nặng (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("ĐỦ ĐIỀU KIỆN")

else:
    print("KHÔNG ĐỦ ĐIỀU KIỆN")

    if donor_age < 18:
        print("- Chưa đủ 18 tuổi")

    if donor_weight < 50:
        print("- Cân nặng dưới 50 kg")