# Number of water fountains
nwf = int (input ("Please input the number of water fountains in the school: "))
# Number of restrooms
nr = int (input ("Please input the number of restrooms in the school: "))
# Number of classrooms
nc = int (input ("Please input the number of classrooms in the school: "))
# Number of libraries
nl = int (input ("Please input the number of libraries in the school: "))
# Number of common areas
nca = int (input ("Please input the number of common areas in the school: "))

print (f"The resource density of water fountains is {nwf / nc}.")
print (f"The resource density of restrooms is {nr / nc}.")
print (f"The resource density of libraries is {nl / nc}.")
print (f"The resource density of common areas is {nca / nc}.")