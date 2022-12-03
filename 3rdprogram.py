# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

l=[]
n=int(input("enter the number of values into list:"))
for i in range(n):
    a=int(input("enter a values:"))
    l.append(a)
def square(x):
    return x**2
print(list(map(square,l)))
