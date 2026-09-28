def quan_ly_lop_hoc():
    lop_hoc = {
        "An": 8.5,
        "Binh": 7.0,
        "Cuong": 9.2
    }

    for i in range(1, 4):
        ten = input(f"Nhap ten hoc sinh thu {i}: ").strip()
        diem = float(input(f"Nhap diem cua {ten}: "))
        lop_hoc[ten] = diem

    avg = sum(lop_hoc.values()) / len(lop_hoc)
    print("Diem trung binh ca lop:", avg)

    print("Hoc sinh co diem > 8:")
    for ten, diem in lop_hoc.items():
        if diem > 8:
            print(f"{ten}: {diem}")

    sorted_hs = sorted(lop_hoc.items(), key=lambda x: x[1], reverse=True)
    print("Danh sach giam dan theo diem:")
    for ten, diem in sorted_hs:
        print(f"{ten}: {diem}")

if __name__ == "__main__":
    quan_ly_lop_hoc()
