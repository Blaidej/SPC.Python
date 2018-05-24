def factorial(n):
    if(n == 0 or n ==0):
        return 1;
    else:
        return n * factorial(n-1)

def main():
    n  =eval(input("Number to find factorial: "))
    print(" The value of the n input: ",n)
    n_fac = factorial(n)
    print("The factorial of n: ", n_fac)

main()

