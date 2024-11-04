lst = [1,2,3,4,5,6]
print(lst)
lst = [i**2 for i in lst]
print(lst)

print('*'*48)

# print even numbers
lst = [ i for i in lst if(i%2==0)]
print(lst)

print('*'*48)

# flattend the list 

ans = [[1,2,3],[4,5,6],[7,8,9]]

ans = [j for i in ans for j in i]
print(ans)