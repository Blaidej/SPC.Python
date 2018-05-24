import math

l1 = [1.0, 2.0, 3.0, 4.0, 5.0]
l2 = [11.0, 62.0, 36.0, 894.0, 455.0]

#find the avedrage of the values in l1 and l2
l1avg = sum(l1) / len(l1)
l2avg = sum(l2) / len(l2)

def sd(a):
    aavg = sum(a) / len(a)
    sumsqdef = 0
    for i in range( 0, len(a)):
        sumsqdef = sumsqdef + (a[i] - aavg)**2

    avgdef = sumsqdef / len(a)

    return math.sqrt(avgdef)

print("Std. Dev. of l1: ", sd(l1))

print("Std. Dev. of l2: ", sd(l2))

