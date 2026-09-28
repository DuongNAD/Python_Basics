def xu_ly_set():
    ds1 = list(map(int, input("Nhap ds 1: ").split()))
    ds2 = list(map(int, input("Nhap ds 2: ").split()))

    set1 = set(ds1)
    set2 = set(ds2)
    print("Set 1:", set1)
    print("Set 2:", set2)

    print("Giao:", set1.intersection(set2))
    print("Hieu (set1 - set2):", set1.difference(set2))
    print("Hop:", set1.union(set2))

if __name__ == "__main__":
    xu_ly_set()
