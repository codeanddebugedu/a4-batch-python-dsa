name = "Anirudh"
age = 55
gender = "Male"

# Method 1
# print("My name is", name)
# print("My age is", age)
# print("My gender is", gender)
# print("My name is", name, "my age is", age, "and my gender is", gender)

# Method 2 (F-Strings)
# print(f"My name is {name}")
# print(f"My age is {age}")
# print(f"My gender is {gender}")
# print(f"My name is {name} my age is {age} and gender is {gender}")

# Method 3 (Identfiers)
"""
%s -> String
%d -> Integer
%f -> Float
"""
print("My name is %s" % name)
print("My age is %d" % age)
print("My gender is %s and done." % gender)
print("My name is %s and age is %d, gender is %s" % (name, age, gender))
