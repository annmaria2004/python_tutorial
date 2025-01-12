def findroot(n):
    ans=1
    for i in range(0,n):
        ans = (n/ans+ans)/2
    return ans
n = int(input("enter the no :\n"))
print("Square root of no :",findroot(n))