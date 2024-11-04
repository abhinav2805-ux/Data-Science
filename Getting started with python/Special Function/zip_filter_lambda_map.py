# zip
lst1 = ['A','B','C']
lst2 = [1,2,3]
print(list(zip(lst1,lst2)))

print('-'*30)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])

print('-'*30)

lsta = [2,4,6]
lstb= [1,3,5]

print([i*j for i,j in zip(lsta,lstb)])

print('-'*30)



  # filter 


def is_even(x):
    return x % 2 == 0

print(list(filter(is_even,[1,2,3,4,5,6,7,8,9,10])))

print('-'*30)


# Lambda

add_num = lambda x,y : x + y
print(add_num(7,9))
print('-'*30)

num = [1,2,3,4,5,6,7,8]
ans = lambda x: x%2==0
print(list(filter(ans,num)))
print('-'*30)

# map
num = [1,2,3,4,5,6,7,8]

def sqr(x):
    return x**2

print(list(map(sqr,num)))

