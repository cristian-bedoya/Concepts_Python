# too_long_list = [x for x in range(10000000000000000)] produce MemoryError
# use  too_long_list = range(10000000000000000)
a = iter(range(10))
b = list(range(10))
print('=========iterable==============')
print(b)
print('========= iter iterator==============')
for i in b:
    print(i)
print('========= reversed iterator==============')
seq_string = 'Python'
print(seq_string)
str1 = reversed(seq_string)
print(next(str1))
print(next(str1))
print(list(str1))
print('========= enumerate iterator==============')
l1 = ["eat","sleep","repeat"]
print(l1)
s1 = "geek"
print(s1)
ob1 = enumerate(l1)
a,b = next(ob1)
print(a,b)
print(next(ob1))
print (list(enumerate(s1,1)))
print('========= zip iterator==============')
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = ("Peter", "Zac", "Alicia")
x = zip(a, b, c)
print(x)
print(next(x))
print(list(x))
print('========= filter iterator==============')
# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filtered_vowels = filter(filter_vowels, letters)

print('The filtered vowels are:')
print('the first is ::', next(filtered_vowels), "::then :")
for vowel in filtered_vowels:
    print(vowel)

print('========= map iterator==============')
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))