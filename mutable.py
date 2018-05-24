# an example of programming mutable arguments
# and formal parameters

# lets show that a list is mutable
l = [45, 23, 65, 44, 56, 76]

print(l)

#l[1] = 99

#print(l)

#variables declared outside of any function# Global variables
b = 9999
c = 11182


def funcMutate(a,b,c):
    a[5] = 999
    b = 88
    c = 90
    #a = [3, 4, 5, 6] this wouldn't change a, it would only be local
    print(b,c)
    return

a1 = l
a2 = 22
a3 = 99



#funcMutate( a1, a2, a3)

#print(a1, a2, a3)

#arguments and formal parameter relationships have been positional

#funcMutate(0, 0, 0)

print(a1, a2, a3)
