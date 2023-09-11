# Filters!

list_of_dict = [
    {"service": "facebook", "password" : "abc123", "added_on" : "21.03.23"},
    {"service": "instagram", "password": "1nstagr@m", "added_on" : "21.03.22"},
    {"service": "bebo", "password": "p@ssword", "added_on" : "10.04.12"},
    {"service": "twitter", "password": "abc123", "added_on" : "19.07.18"},
    {"service": "tiktok", "password": "rubbish", "added_on" : "30.09.23"}
]
# using a for loop:
def find_facebook_1(dict):
    for password in dict:
        if password['service'] == 'facebook':
            return password

method1 = find_facebook_1(list_of_dict)
print(f"Method 1: {method1}")

# Using "filter"
def is_facebook_2(password):
    return password["service"] == "facebook"

method2 = next(filter(is_facebook_2, list_of_dict))
print(f"Method 2: {method2}")

# Using lambda
method3 = next(filter(lambda plist: plist["service"] == "facebook", list_of_dict))

print(f"Method 3: {method3}")

# List comprehension
method4 = [entry for entry in list_of_dict if entry["service"] == "facebook"]

print(f"Method 4: {method4}")


########################
# Practice
# Write a function that checks whether any passwords were added on 21/03/22

# for loop

def check_added_21_march_22(list):
    for entry in list:
        if entry["added_on"] == "21.03.22":
            return True
        else:
            continue
    return False
        
print(check_added_21_march_22(list_of_dict))

# using filter - check for passwords which are abc123

def check_simple_passwords(list):
    return list["password"] == "abc123"

print(list(filter(check_simple_passwords, list_of_dict))) #all of them
print(next(filter(check_simple_passwords, list_of_dict))) # just the first one

# Using lambda

print(list(filter(lambda entry: entry["password"] == "1nstagr@m", list_of_dict)))

# Using list comprehension
alphabet_only = [entry for entry in list_of_dict if entry["password"].isalpha() == True]

print(alphabet_only)

result = map(lambda number: number * 2, [1, 2, 3, 4])
print(list(result))