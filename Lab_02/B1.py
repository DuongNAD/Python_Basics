def find_max(arr):
    max_val = max(arr)
    return max_val

if __name__ == '__main__':
    arr = [1, -5, 3, 4, 7, 6, -7, 8, 9, 33]
    max_val = find_max(arr)
    print(max_val)
    if max_val % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if max_val % 3 == 0:
        print("Chia het cho 3")
    else:
        print("K chia het cho 3")

    if max_val < 0:
        print("Negative")
    elif max_val > 0:
        print("Positive")
    else:
        print("Zero")