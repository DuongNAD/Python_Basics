"""
PYTHON LAB 01: CÁC KHÁI NIỆM CƠ BẢN, BIẾN, KIỂU DỮ LIỆU & TOÁN TỬ
Lớp: AAHN_C2411L
Học viên: Nguyễn Anh Dương
Giảng viên: Thầy Thắng (Thang Dao Manh)
"""

import sys

# Hỗ trợ hiển thị tiếng Việt có dấu chuẩn xác trên console Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass


def cau_1():
    """Câu 1: In dòng chữ Hello, Python! và tên của bạn."""
    print("--- CÂU 1: XUẤT DỮ LIỆU CƠ BẢN ---")
    print("Hello, Python!")
    print("Nguyễn Anh Dương")


def cau_2():
    """Câu 2: Liệt kê 5 tên biến trong Python (ít nhất 2 tên không hợp lệ) & giải thích."""
    print("--- CÂU 2: QUY TẮC ĐẶT TÊN BIẾN TRONG PYTHON ---")
    print("\n[+] 3 tên biến HỢP LỆ:")
    print("1. 'ho_ten'         -> Hợp lệ: Chỉ gồm chữ cái, dấu gạch dưới theo chuẩn snake_case.")
    print("2. 'tuoi_sinh_vien' -> Hợp lệ: Bắt đầu bằng chữ cái, mang tính gợi nhớ rõ ràng.")
    print("3. '_diem_so'       -> Hợp lệ: Python cho phép tên biến bắt đầu bằng dấu gạch dưới (_).")

    print("\n[-] 2 tên biến KHÔNG HỢP LỆ & Giải thích lý do:")
    print("4. '2ban'           -> KHÔNG HỢP LỆ: Tên biến không được phép bắt đầu bằng chữ số (gây SyntaxError).")
    print("5. 'ten-sinh-vien'   -> KHÔNG HỢP LỆ: Chứa ký tự đặc biệt '-' (dấu gạch ngang), Python hiểu nhầm là phép trừ.")
    print("   * Lưu ý thêm: Không được đặt tên biến trùng từ khóa (keywords) như 'class', 'def', 'if', 'while'...")


def cau_3():
    """Câu 3: Khai báo các biến (chuỗi, số nguyên, số thực, boolean) và in giá trị + kiểu dữ liệu."""
    print("--- CÂU 3: CÁC KIỂU DỮ LIỆU CƠ BẢN ---")
    ten = "Nguyễn Anh Dương"
    tuoi = 20
    chieu_cao = 1.70
    trang_thai_hoc = True

    print(f"Tên: {ten} | Kiểu: {type(ten)}")
    print(f"Tuổi: {tuoi} | Kiểu: {type(tuoi)}")
    print(f"Chiều cao: {chieu_cao} | Kiểu: {type(chieu_cao)}")
    print(f"Trạng thái đang học: {trang_thai_hoc} | Kiểu: {type(trang_thai_hoc)}")


def cau_4():
    """Câu 4: Nhập tên và tuổi từ bàn phím, in lời chào."""
    print("--- CÂU 4: NHẬP XUẤT VỚI INPUT ---")
    ten = input("Nhập tên: ").strip()
    tuoi = input("Nhập tuổi: ").strip()
    print(f"Chào {ten}, bạn {tuoi} tuổi.")


def cau_5():
    """Câu 5: Nhập vào 2 số, tính tổng, hiệu, tích, thương."""
    print("--- CÂU 5: CÁC PHÉP TOÁN SỐ HỌC CƠ BẢN ---")
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        print(f"Tổng ({a} + {b}): {a + b}")
        print(f"Hiệu ({a} - {b}): {a - b}")
        print(f"Tích ({a} * {b}): {a * b}")
        if b != 0:
            print(f"Thương ({a} / {b}): {a / b}")
        else:
            print("Thương: Không thể chia cho 0 (ZeroDivisionError)!")
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số!")


def cau_6():
    """Câu 6: Nhập hai số, so sánh số thứ nhất lớn hơn không? hai số bằng nhau không?"""
    print("--- CÂU 6: TOÁN TỬ SO SÁNH ---")
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        print("Số thứ nhất có lớn hơn số thứ hai không?", a > b)
        print("Hai số có bằng nhau không?", a == b)
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số!")


def cau_7():
    """Câu 7: Ép kiểu dữ liệu giữa int, float, str."""
    print("--- CÂU 7: ÉP KIỂU DỮ LIỆU (TYPE CASTING) ---")
    val_int = 10
    val_float = 15.5
    val_str = "100"

    res1 = float(val_int)
    res2 = int(val_float)
    res3 = str(val_int)

    print(f"int sang float: {res1} | Kiểu: {type(res1)}")
    print(f"float sang int: {res2} | Kiểu: {type(res2)}")
    print(f"int sang str  : '{res3}' | Kiểu: {type(res3)}")


def cau_8():
    """Câu 8: Nhập vào một số nguyên, kiểm tra chẵn hay lẻ."""
    print("--- CÂU 8: CẤU TRÚC ĐIỀU KIỆN KIỂM TRA CHẴN LẺ ---")
    try:
        n = int(input("Nhập một số nguyên: "))
        if n % 2 == 0:
            print(f"Số {n} là số chẵn")
        else:
            print(f"Số {n} là số lẻ")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


def cau_9():
    """Câu 9 (Mở rộng): Nhập họ tên, tách họ, tên đệm và tên."""
    print("--- CÂU 9 (MỞ RỘNG): XỬ LÝ CHUỖI TÁCH HỌ TÊN ---")
    ho_ten = input("Nhập họ và tên: ").strip()
    parts = ho_ten.split()
    ho = parts[0] if len(parts) > 0 else ""
    ten = parts[-1] if len(parts) > 1 else ""
    ten_dem = " ".join(parts[1:-1]) if len(parts) > 2 else ""

    print("Họ     :", ho)
    print("Tên đệm:", ten_dem)
    print("Tên    :", ten)


def cau_10():
    """Câu 10 (Mở rộng): Lũy thừa và chia lấy dư."""
    print("--- CÂU 10 (MỞ RỘNG): TOÁN TỬ LŨY THỪA & CHIA LẤY DƯ ---")
    try:
        a = int(input("Nhập số nguyên thứ nhất: "))
        b = int(input("Nhập số nguyên thứ hai: "))
        print(f"Lũy thừa ({a} ** {b}): {a ** b}")
        if b != 0:
            print(f"Phần dư ({a} % {b}): {a % b}")
        else:
            print("Không thể chia lấy dư cho 0!")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


def main():
    while True:
        print("\n" + "=" * 50)
        print("       PYTHON LAB 01 - MENU CHẠY BÀI TẬP")
        print("=" * 50)
        print(" 1. Câu 1 : In Hello, Python! và tên")
        print(" 2. Câu 2 : Tên biến hợp lệ / không hợp lệ (Lý thuyết)")
        print(" 3. Câu 3 : Khai báo biến & in kiểu dữ liệu")
        print(" 4. Câu 4 : Nhập tên, tuổi & in lời chào")
        print(" 5. Câu 5 : Tổng, hiệu, tích, thương 2 số")
        print(" 6. Câu 6 : So sánh 2 số")
        print(" 7. Câu 7 : Ép kiểu dữ liệu (int, float, str)")
        print(" 8. Câu 8 : Kiểm tra số chẵn hay số lẻ")
        print(" 9. Câu 9 : Tách họ, tên đệm, tên chính (Mở rộng)")
        print("10. Câu 10: Tính lũy thừa và chia lấy dư (Mở rộng)")
        print(" 0. Thoát chương trình")
        print("=" * 50)

        choice = input("👉 Nhập số câu muốn chạy (0 để thoát): ").strip()
        if choice == "0":
            print("\n👋 Kết thúc chương trình Lab 01. Chúc bạn học tốt!")
            break

        func_map = {
            "1": cau_1,
            "2": cau_2,
            "3": cau_3,
            "4": cau_4,
            "5": cau_5,
            "6": cau_6,
            "7": cau_7,
            "8": cau_8,
            "9": cau_9,
            "10": cau_10
        }

        if choice in func_map:
            print("\n" + "-" * 50)
            func_map[choice]()
            print("-" * 50)
        else:
            print("⚠️ Lựa chọn không hợp lệ! Vui lòng nhập từ 0 đến 10.")


if __name__ == "__main__":
    main()
