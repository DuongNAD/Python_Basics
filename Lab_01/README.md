# Lab 01: Nhập Môn Python - Biến, Kiểu Dữ Liệu & Toán Tử

- **Lớp**: `AAHN_C2411L`
- **Môn học**: Python Programming
- **Giảng viên**: Thầy Thắng (Thang Dao Manh)
- **Học viên**: Nguyễn Anh Dương

---

## 📌 Danh Sách Đề Bài & Nội Dung Chi Tiết

| Câu | Nội Dung Đề Bài | Trạng Thái |
|:---:|---|:---:|
| **Câu 1** | Viết chương trình in ra dòng chữ `Hello, Python!` và tên của bạn. |  Hoàn thành |
| **Câu 2** | Liệt kê 5 tên biến trong Python, trong đó có ít nhất 2 tên không hợp lệ. Giải thích tại sao. |  Hoàn thành |
| **Câu 3** | Khai báo các biến: Tên (chuỗi), Tuổi (số nguyên), Chiều cao (số thực), Trạng thái đang học (boolean). In ra giá trị và kiểu dữ liệu từng biến. |  Hoàn thành |
| **Câu 4** | Nhập vào tên và tuổi từ bàn phím. In ra câu: `Chào <tên>, bạn <tuổi> tuổi.` |  Hoàn thành |
| **Câu 5** | Nhập 2 số từ bàn phím. Tính và in ra tổng, hiệu, tích và thương của 2 số đó (có kiểm tra chia cho 0). |  Hoàn thành |
| **Câu 6** | Nhập 2 số. So sánh và in kết quả: Số thứ nhất có lớn hơn số thứ hai không? Hai số có bằng nhau không? |  Hoàn thành |
| **Câu 7** | Tạo ba biến kiểu `int`, `float`, `str`. Chuyển đổi: `int -> float`, `float -> int`, `int -> str`. In kết quả ra màn hình. |  Hoàn thành |
| **Câu 8** | Nhập vào một số nguyên. Kiểm tra số đó là chẵn hay lẻ. |  Hoàn thành |
| **Câu 9** *(Mở rộng)* | Nhập họ và tên đầy đủ, tách thành: Họ, Tên đệm, Tên chính. |  Hoàn thành |
| **Câu 10** *(Mở rộng)* | Nhập 2 số nguyên, tính lũy thừa ($a^b$) và phép chia lấy dư ($a \pmod b$). |  Hoàn thành |

---

## 📖 Chi Tiết Lời Giải Lý Thuyết Câu 2

### 1. 3 Tên biến HỢP LỆ trong Python:
1. `ho_ten`: Bắt đầu bằng chữ cái, các từ ngăn cách nhau bằng dấu gạch dưới `_` (chuẩn đặt tên PEP 8 - snake_case).
2. `tuoi_sinh_vien`: Chỉ chứa chữ cái và số/gạch dưới, mang ý nghĩa trực quan, gợi nhớ.
3. `_diem_so`: Python cho phép tên biến bắt đầu bằng dấu gạch dưới `_` (thường dùng trong quy ước private variable trong class).

### 2. 2 Tên biến KHÔNG HỢP LỆ & Giải thích:
1. `2ban`: **KHÔNG HỢP LỆ**. Trong Python, tên biến không được phép bắt đầu bằng một chữ số. Nếu khai báo sẽ gây lỗi cú pháp `SyntaxError: invalid decimal literal`.
2. `ten-sinh-vien`: **KHÔNG HỢP LỆ**. Tên biến không được chứa các ký tự đặc biệt ngoài dấu gạch dưới `_`. Ký tự `-` (dấu gạch ngang) sẽ bị trình thông dịch hiểu nhầm là toán tử trừ (`-`), gây lỗi cú pháp `SyntaxError: cannot assign to expression here`.

> **Lưu ý bổ sung**: Tên biến cũng không được trùng với các từ khóa dành riêng (keywords) của Python như: `class`, `def`, `if`, `else`, `while`, `for`, `import`, `return`, `True`, `False`, `None`...

---

## 🚀 Hướng Dẫn Chạy Bài Tập

Mở terminal tại thư mục này và thực thi:

```bash
# Di chuyển vào thư mục Lab 01 (nếu đang ở thư mục gốc)
cd Lab_01

# Chạy file bài tập có menu tương tác
python bai_tap.py
```

Chương trình sẽ hiển thị menu tương tác từ `0` đến `10`, cho phép bạn chọn chạy thử bất kỳ câu nào tùy ý.
