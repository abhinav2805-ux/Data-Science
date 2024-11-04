n = 0
count = 1
sum = 0
while(sum<30):
    sum+=n
    n+=1
    print(count,"counter")
    count+=1
print(sum,"this is the sum")     


s = "vanihba"
i=len(s)-1
while(i>=0):
    print(s[i],end='')
    i-=1

print('#'*20)

p=0

a = 12345
while(a>0):
    x = a%10
    p+=x
    print(x,end='')
    a = a//10    
print(p)    