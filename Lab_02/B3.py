def bang_cuu_chuong(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

if __name__ == "__main__":
    while True:
        n= int(input())
        if(n >=2 and n <=9):
            break
        print("So k hop le")
    bang_cuu_chuong(n)