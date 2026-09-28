def thong_tin_sinh_vien():
    student = {
        "name": "Nguyen Anh Duong",
        "age": 20,
        "major": "Information Technology"
    }
    print("Thong tin sinh vien:", student)

    student["major"] = "Artificial Intelligence"
    print("Major sau cap nhat:", student["major"])

    student["gpa"] = 3.8
    print("GPA:", student["gpa"])

    for key, value in student.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    thong_tin_sinh_vien()
