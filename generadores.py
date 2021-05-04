def generate_even(limit):
    num = 1
    my_list = []
    while num < limit:
        my_list.append(num*2)
        num += 1
    return my_list

def generate_even_gf(limit):
    num = 1
    while num < limit:
        yield num * 2
        num += 1
print('=========normal function==============')
print((generate_even(10)))
# get even is the object that save the even number from genenrator function
get_even = generate_even_gf(10)
print(type(get_even))

print('=========generator function===========')
# for i in get_even:
#     print(i)

while get_even:
    try:
        print(next(get_even)) 
    except:
        break

# *cities means that receipt undetermined cities in a tupple
def get_cities(*cities):
    for city in cities:
        yield from city

give_cities = get_cities("medellin", "cali", "bogota", "barranquilla")
print(next(give_cities))
print(next(give_cities))
