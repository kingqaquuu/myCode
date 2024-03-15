def is_palindrome(n):
    temp=n
    total=0
    while temp>0:
        total=total*10+temp%10
        temp//=10
    return total==n
def is_prime(n):
    if n<=1:
        return False
    for factor in range(2,int(n**0.5)+1):
        if n%factor==0:
            return False
    return True
n=int(input('n='))
print(is_palindrome(n))
print(is_prime(n))
print(is_palindrome(n) and is_prime(n))