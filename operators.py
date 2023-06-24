# Arithmatic operators
x = 5
y = 2
print(x + y, x / y, x * y, x % y, x - y, x ** y)

# Comparison Operator

print(x > y, x < y, x == y, x != y, x >= y, x <= y)

# Assignment Operators

c = 10
d = 1
c += d  # c= c+d
c -= d  # c= c-d
print(c)

# Logical Operator

a = 40
b = 60
x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (a > b) or (x < y)
print(out)

out = (a > b) or (x > y)
print(out)

out = (a < b) and (x > y)
print(out)

out = (a > b) and (x < y)
print(out)

out = (a > b) and (x > y)
print(out)

out = not ((a > b) and (x > y))
print(out)

# Membership Operator
str1 = "Hello world"
first_tuple = ("asd gjh jklj", 47, 12, 1.5)
ans = "gjh" in first_tuple
print(ans)
ans = "asd gjh jklj" in first_tuple
print(ans)
ans = 12 in first_tuple
print(ans)

first_tuple = ("asd gjh jklj", 47, 12, 1.5)
ans = "gjh" not in first_tuple
print(ans)
ans = "asd gjh jklj" not in first_tuple
print(ans)
ans = 12 not in first_tuple
print(ans)

# Identity Operator
a = 12
b = 15
print(a is b)
print(a is not b)
