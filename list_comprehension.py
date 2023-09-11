number_list = [54, 36, 23, 99, 71, 20, 37, 85, 42]

all = [num for num in number_list] # copies the list - iterates over each num in number_list and adds it

evens = [num for num in number_list if num % 2 == 0] #This time, num is only copied if it is even

multiples_of_3 = [num for num in number_list if num % 3 == 0] # This time only if it's divisible by 3

add_1 = [num+1 for num in number_list] # This one adds 1 to the number when it is copied

add_1_to_odds = [num+1 for num in number_list if num % 2 == 1] # This one only adds 1 to the odd numbers

print(f"all: {all}")
print(f"evens: {evens}")
print(f"multiples of 3: {multiples_of_3}")
print(f"add 1 to all: {add_1}")
print(f"add 1 to odds only: {add_1_to_odds}")
