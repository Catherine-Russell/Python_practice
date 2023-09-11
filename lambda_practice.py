def my_map(function, iterable):
    result = []
    for item in iterable:
        new_item = function(item)
        result.append(new_item)
    return(result)

numbers = [1, 2, 3, 4, 5]

cubed = my_map(lambda x: x**3, numbers)
add_1 = my_map(lambda x: x + 1, numbers)
multiply_by_5 = my_map(lambda x: x * 5, numbers)


print(cubed)
print(add_1)
print(multiply_by_5)
