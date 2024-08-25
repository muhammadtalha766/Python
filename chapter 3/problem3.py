# find double spacing in the code

name = "Hi, Friends this  is Talha. How  are you?"
# find() method is use to find the index

print(name.find("  "))
print(name.find("th"))

# fix double space 
print(name.replace("  ", " "))

# note : string are immeutable
print(name)