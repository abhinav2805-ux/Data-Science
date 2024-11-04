# Implicit typecasting from int to float
integer_number = 5
float_number = 3.14
result = integer_number + float_number
print(result)  # Output: 8.14
# The integer is implicitly converted to a float before the addition.


# Attempted implicit typecasting from int to string
integer_number = 10
string_number = "5"
# Uncommenting the line below will raise an error:
# result = integer_number + string_number
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Converting int to float
integer_number = 41
float_number = float(integer_number)
print(float_number, type(float_number))  # Output: 41.0 <class 'float'>

# Converting float to int
float_value = 7.12
int_value = int(float_value)
print(int_value, type(int_value))  # Output: 7 <class 'int'>

# Converting int to str
integer_value = 123
str_value = str(integer_value)
print(str_value, type(str_value))  # Output: 123 <class 'str'>


# Converting a tuple to a list
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print(list_data)  # Output: [1, 2, 3]


# Converting a list to a set
list_data = [1, 2, 3]
set_data = set(list_data)
print(set_data)  # Output: {1, 2, 3}
