lst = [
    [
        ["Alice", 85],
        ["Bob", 90],
        ["Charlie", 78]
    ],
    [
        ["David", 92],
        ["Eva", 88],
        ["Frank", 76]
    ],
    [
        ["Grace", 89],
        ["Hannah", 95],
        ["Ian", 82]
    ]
]

print(lst[0][1])

print('*'*48)

print(lst)
print('*'*48)

# modified from  previous list
lst[0][1][0] = "Alex"
print(lst)

# change in the list 
lst[1] = [1, 2, 3, 4, 5]
print(lst)
print('*'*48)

# delete the index
del lst[0]
print(lst)
print('*'*48)

# reverse
print(lst[::-1])
print('*'*48)

