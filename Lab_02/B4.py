def is_prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def prime_number(n):
    arr =[]
    for i in range(2,n//2+1):
        if n%i==0:
            arr.append(i)
    return arr

if __name__ == '__main__':
    n = int(input())
    check = is_prime(n)
    if check:
        print("Day la so nguyen to")
    else:
        print("Day k phai la so nguyen to")
        print(prime_number(n))