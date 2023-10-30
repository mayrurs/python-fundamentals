# Int 
a = 1 
b = a
b = 2
print(a, b)

# Float
a = 1.0
b = a
b = 2.0
print(a, b)

# String
a = "abc"
b = a
# b[2] = "d"
b = "cde"
print(a, b)

# List
a = [1,2,3]
b = a
b[0] = 5
print(a, b)
b = [5, 6, 7]
print(a,b)

# Tuple 
a = 1, 2, 3
b = a 
# b[0] = 0
b = 4, 5, 6
print(a, b)

# Dict 
d = {'a': 1, 'b': 2}
e = d
e['a'] = 4
print(d, e)
e = {'c': 5, 'd': 6}
print(d, e)

