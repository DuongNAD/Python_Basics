def xu_ly_tuple():
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print("Phan tu dau tien:", days[0])
    print("Phan tu cuoi cung:", days[-1])
    for d in days:
        print(d)
    if "Sunday" in days:
        print("Co Sunday trong tuple")
    else:
        print("Khong co Sunday trong tuple")
    temp = list(days)
    temp.append("Holiday")
    days = tuple(temp)
    print("Tuple moi:", days)

if __name__ == "__main__":
    xu_ly_tuple()
