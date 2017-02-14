t=int(raw_input())
a=list()
for i in range(0,t):
    n=int(raw_input())
    r=int(raw_input())
    for j in range(0,n):
        l=int(raw_input())
        a.append(l)
    for j in range(r,n):
        print(a[j])
        print(" ")
    for j in range(0,r):
        print(a[j])
        print(" ")
