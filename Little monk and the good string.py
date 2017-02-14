a=raw_input()

n=len(a)
count=0
max=0

for i in range(0,n):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i'or a[i]=='o'or a[i]=='u'):
        count=count+1
        if(count>max):
             max=count
    else:
        count=0

print(max)