def superify(name):
    return "super" + name

super_person = input("Say a name of someone super: ")

print(superify(super_person))

# Don't edit below this line.

dog_result = superify("dog")
#print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
#print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"