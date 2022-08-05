x = [1,1,1,1,1,1,13,3,4,5,6,6,555,4,4,4,]

print('total no of 3 = ',x.count(3))
print('total no of 1 = ',x.count(1))
print('total no of 4 = ',x.count(4))

movies=['batman','ddlj','man in black','krish','golmaal','doc strange','3idiots','jab we met','puspa','kgf','rrr']
print(movies.index('man in black'))

# print(movies.index('kunfu panda'))
blockbusters=movies.copy()
print('duplicate list=',blockbusters)

blockbusters.clear()
print('after clearing blockbusters=',blockbusters)

print('after poping = ',movies.pop())
print('after poping index 4 = ',movies.pop(4))
print('after poping index 7 = ',movies.pop(7))
print('after poping unavailbe index=',movies.pop(8))

