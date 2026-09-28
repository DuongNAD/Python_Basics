# 🐍 Python Basics - Khóa Học Lập Trình Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Class-AAHN__C2411L-brightgreen.svg" alt="Class" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange.svg" alt="Status" />
  <img src="https://img.shields.io/badge/Author-Nguyen%20Anh%20Duong-purple.svg" alt="Author" />
</p>

Repository lưu trữ toàn bộ mã nguồn, bài tập thực hành theo từng buổi học (Labs / Assignments) của khóa học Lập trình Python.

---

## 📂 Quy Hoạch Cấu Trúc Thư Mục (Folder Structure)

Dự án được quy hoạch theo từng buổi thực hành (`Lab_XX/`) một cách khoa học, độc lập và dễ quản lý:

```text
Python/
├── .gitignore                   # Cấu hình bỏ qua cache, virtualenv, file tạm
├── README.md                    # Tổng quan repository & mục lục tiến độ học
├── Lab_01/                      # Buổi 1: Tổng quan, Biến, Kiểu dữ liệu & I/O
│   ├── README.md                # Tóm tắt đề bài, lý thuyết và hướng dẫn chạy
│   └── bai_tap.py               # Toàn bộ code bài tập 1-10 kèm Menu tương tác
└── Lab_02/                      # Buổi 2: Cấu trúc điều khiển & Cấu trúc dữ liệu
    ├── README.md                # Tóm tắt 10 bài tập Lab 02
    └── B1.py -> B10.py          # Code từng bài tập từ B1 đến B10
```

*Các buổi học tiếp theo (`Lab_03/`, ...) sẽ tiếp tục được cập nhật theo cấu trúc chuẩn tương tự.*

---

## 📑 Mục Lục Các Buổi Lab & Tiến Độ Học Tập

| Buổi / Lab | Chủ Đề Bài Học | Nội Dung Trọng Tâm | Trạng Thái | Link Chi Tiết |
|:---:|---|---|:---:|:---:|
| **Lab 01** | Nhập môn Python & Cú pháp cơ bản | Khai báo biến, kiểu dữ liệu (`int`, `float`, `str`, `bool`), nhập xuất `input()` / `print()`, toán tử số học & so sánh | ✅ Hoàn thành | [Xem Lab 01](Lab_01/README.md) |
| **Lab 02** | Cấu trúc rẽ nhánh, Vòng lặp & Cấu trúc dữ liệu | `if-elif-else`, vòng lặp `for`, `while`, thao tác List, Tuple, Dictionary, Set | ✅ Hoàn thành | [Xem Lab 02](Lab_02/README.md) |
| **Lab 03** | Cấu trúc dữ liệu nâng cao | List comprehension, nested structures, sorting nâng cao | ⏳ Sắp tới | - |
| **Lab 04** | Hàm & Xử lý Ngoại lệ | Định nghĩa hàm (`def`), tham số (`*args`, `**kwargs`), `try-except-finally` | ⏳ Sắp tới | - |
| **Lab 05** | Thao tác File & Module | Đọc/ghi file (`txt`, `csv`, `json`), import thư viện chuẩn | ⏳ Sắp tới | - |
| **Lab 06** | Lập trình hướng đối tượng (OOP) | Class, Object, Kế thừa, Đóng gói, Đa hình | ⏳ Sắp tới | - |

---

## 🛠 Hướng Dẫn Cài Đặt & Chạy Code

### 1. Yêu Cầu Môi Trường
- Đã cài đặt **Python 3.8+** trên máy tính ([Tải tại python.org](https://www.python.org/)).
- Kiểm tra phiên bản Python:
  ```bash
  python --version
  ```

### 2. Clone Repository
```bash
git clone https://github.com/DuongNAD/Python_Basics.git
cd Python_Basics
```

### 3. Thực Thi Bài Tập (Ví dụ Lab 01)
```bash
cd Lab_01
python bai_tap.py
```
> Chương trình sẽ mở ra Menu tương tác số, bạn chỉ cần gõ số câu (từ `1` đến `10`) để chạy kiểm tra trực tiếp.

---

## 👤 Thông Tin Học Viên
- **Học viên**: Nguyễn Anh Dương
- **Lớp**: AAHN_C2411L
- **GitHub**: [@DuongNAD](https://github.com/DuongNAD)
