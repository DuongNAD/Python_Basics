def xu_ly_list():
    ds = list(map(int, input("Nhap danh sach so nguyen: ").split()))
    print("So phan tu:", len(ds))
    if not ds:
        return
    print("Tong:", sum(ds))
    print("Trung binh:", sum(ds) / len(ds))
    print("Tang dan:", sorted(ds))
    if 10 in ds:
        print("Vi tri so 10:", ds.index(10))
    else:
        print("Khong co so 10 trong danh sach")

if __name__ == "__main__":
    xu_ly_list()
