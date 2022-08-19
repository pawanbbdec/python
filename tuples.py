my_tuple = (1,'hello',3.4)
print(my_tuple)

# nested tuple

my_tuple = ('mouse',[8,4,6],(1,2,3))
print(my_tuple)

# a tuple can also be created without using parentheses.
my_tuple = 3,4.6,'apple'
print(my_tuple)

# nested tuple

n_tuple = ('mouse', [8,4,6],(1,2,3,))
#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

# accessing tuple elements using slicing

my_tuple = ('e','x','c','a','1','i','b','u','r')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

#concatenation
my_tuple = (1,2,3,4,5,6)
print((1,2,3) + (4,5,6))

my_tuple = ('a','p','p','1','e')
print(my_tuple.count('p'))
print(my_tuple.index('1'))
