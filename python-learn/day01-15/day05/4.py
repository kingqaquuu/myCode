for x in range(1,10000):
    ans=0
    for y in range(1,x):
        if x%y==0:
            ans=ans+y
    if ans==x:
        print(x)