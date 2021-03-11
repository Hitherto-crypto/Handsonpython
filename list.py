squares=[1,4,9,16,25]
print(squares)
squares[0] # indexing returns the item
print(squares[0])
squares[-3:] # slicing returns a new list
print(squares[-3:])
squares[:]
print(squares[:])
squares + [36,49,64,81,100]
print(squares + [36,49,64,81,100])

cubes=[1,8,27,65,125] # something's wrong here
4**3 #the cube of 4 is 64, not 65!
print(4**3)
cubes[3]=64 # replace the wrong value
print(cubes)

cubes.append(216) # add the cube of 6
cubes.append(7**3) # and the cube of 7
print(cubes)

letters=['a','b','c','d','e','f','g']
print(letters)
# replace some values
letters[2:5]=['C','D','E']
print(letters)
# now remove them
letters[2:5]=[]
print(letters)
#clear the list by relacing all the elementswith an empty list
letters[:]=[]
print(letters)
letters=['a','b','c','d']
print(len(letters))

a=['a','b','c','d']
n=[1,2,3]
x=[a,n]
print(x)
x[0]
print(x[0])
x[0][1]
print([x[0][1]])