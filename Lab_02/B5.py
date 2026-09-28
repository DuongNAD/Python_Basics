def sum_caculate(a,b):
    sum = a + b
    return sum

def diff_caculate(a,b):
    diff = a - b
    return diff

if __name__=="__main__":
    while(True):
        print("1. Tinh tong 2 so")
        print("2. Tinh hieu 2 so")
        print("3. Thoat")
        print("enter number: ")
        n = int(input())

        if(n==1):
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print(sum_caculate(a,b))
        elif(n==2):
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print(diff_caculate(a,b))
        elif(n==3):
            print("Thanks")
            break
        else:
            print("Error")
