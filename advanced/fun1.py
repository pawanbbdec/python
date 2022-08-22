#syntax
# def fun_name([parameter]):
#  statements
# [return expression]

# defininf

def hello():
    print('hello')
    print('world🌎')

#calling or using

hello()
hello()

def greetings(message):
    print(message,'😍')
greetings('world')
greetings('hola amigos')
greetings('bonjur amis')
greetings('namaste dosto')
def calc_area(w,h):
    area = w*h
    print('area:',area)

calc_area(10,20)
calc_area(3,5)
calc_area(100,200)

def calc_area_v2(w,h):
    area = w*h
    return area
#display
print(calc_area_v2(10,20))    
print(calc_area_v2(3,5))    
# storing return value

ans  = calc_area_v2(10,20)
print(ans)
# using return value ina expression
ans = calc_area_v2(3,5)+calc_area_v2(10,2)
print(ans)
