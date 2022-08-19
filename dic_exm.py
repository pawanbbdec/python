my_dict = {'name':'jack','age': 22}
print(my_dict['name'])
print(my_dict.get('age'))



# use get() for key extraction
print(my_dict.get('address'))

#update value
my_dict['age'] = 27
print(my_dict)

my_dict['address'] = 'downtown'
print(my_dict)
squares ={1:1,2:4,3:9,4:16,5:25}

print(squares.pop(4))

print(squares.popitem())
squares.clear()
del squares
squares ={1:1,2:4,3:9,4:16,5:25}

for i  in squares:
    print(i)
# only values using i as key    
for i in squares:
    print(squares[i]) 
    # using function to get both key and value 
for k,v in squares.items():
    print(k,v)  



students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
        sname = input("Enter names of student :")
        marks= []
        for j in range(5):
           mark = float(input("Enter marks :"))
           marks.append(mark)
        students[sname] = marks
print("Dictionary of student created :")
print(students)        
