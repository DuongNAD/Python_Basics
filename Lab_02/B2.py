def sum_even(n):
    sum = 0
    for i in range(n+1):
        if(i % 2 == 0):
            sum += i
    return sum

def number_even(n):
    arr =[]
    for i in range(n+1):
        if(i % 2 == 0):
            arr.append(i)
    return arr

if __name__ == '__main__':
    n = int(input())
    sum_n_even = sum_even(n)
    print(sum_n_even)
    if sum_n_even > 100:
        print("Tong lon")
    else:
        print("Tong nho")

    print(number_even(n))