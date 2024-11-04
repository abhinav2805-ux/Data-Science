# creating a set 
st = {1,2,3,3,4,5,6}
print(st , type(st))
print('-'*48)

# adding
st.add(8)
print(st)

# removing
st.remove(8)
print(st)

print('-'*48)

# cheking value
print(8 in st)
print(4 in st)

print('-'*48)

# set operation

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

print('-'*48)






# tuples 

tpl = (1, 2, 3, 4, 5, 6, 7, 8)
print(tpl)
print('-'*48)

# accessing

print(tpl[0])
print(tpl[1:4])

print('-'*48)

# concatenating

tpl2 = (9, 10, 11, 12)
tpl3 = tpl + tpl2
print(tpl3)

print('-'*48)

# checking

print(3 in tpl)
print(19 in tpl3)

print('-'*48)

# check count

print(tpl.count(3))

print('-'*48)

# finding

print(tpl.index(3))

print('-'*48)

# reversing

print(tpl[::-1])

print('-'*48)

# Multiply

print(tpl * 3)

print('-'*48)


