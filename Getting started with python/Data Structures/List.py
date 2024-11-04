lst = ['abhinav','ankur','riya','parag','avneet']
print(lst)

# access element by using indexing
print(lst[2])
print(lst[-1])

print(lst)

# modify element by using indexing

lst[2] = 'ankita'
print(lst)


#slicing
print(lst[2:6])
print('*'*48)

# reverse 

print(lst[::-1])

# append

lst.append('praveen')
print(lst)
print('*'*48)
# removing elements
print('*'*48)
lst.remove('ankur')
print(lst)
print('*'*48)

#length
print(len(lst))
print('*'*48)

# sort
print(sorted(lst))

# find elements
print(lst.index('avneet'))
print('*'*48)

# count elements
print(lst.count('avneet'))

# extend
print(lst)
lst.extend(['raju','rina','hilihui'])
print(lst)
print('*'*48)

# iterating through elements
for l in lst:
    print(l)

print('*'*48)

# iterating through indexes
for i in range(0,len(lst),1):
    print(lst[i])
print('*'*48)

# iterating in reverse order

for i in range(len(lst)-1,-1,-1):
    print(lst[i])
        