n = int(input("N prime numbers"))
initial = 2
while n!=0:
    for i in range (2,initial):
        if initial%i==0:
            break
    else:
        print(initial)
        n=n-1
    initial = initial+1