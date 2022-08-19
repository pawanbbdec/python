# set of integers
my_set = {1,2,3}
print(my_set)
# set of mixed datatypes

my_set = {1.0,'oye',(1,2,3)}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)

my_set = {1,2,3,4,3,2}
print(my_set)


a = set()
print(type(a))

my_set = {1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([2,3,4])
print(my_set)

#add list and set
my_set.update([4,5],{1,6,8})
print(my_set)

#initialize my_set
my_set = {1,3,4,5,6}
print(my_set)

#discard an element
my_set.discard(4)
print(my_set)
#remove an element
my_set.remove(6)
print(my_set)

#pops a random item
my_set.pop()
print(my_set)

#clear

my_set.clear()
print(my_set)

