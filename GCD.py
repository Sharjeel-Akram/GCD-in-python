# Write Python function GCD(n, m) where n ≥ m. 
# Relatively prime integers are the integers whose GCD is 1. Using the GCD(n,m) function as the 
# building block, write a function rel_prime(n) which will compute the probability that two 
# randomly chosen integers lesser than a given integer n will be relatively prime. User will call this 
# function and pass the input.

#Code for GCD
def gcd(n,m):
    if n % m == 0:
        return m
    else:
        return gcd(m,n%m)

#code to check Probality:
def Real_Prime(K):
    Total_Prime = 0
    Relative_Prime = 0
    for i in range(2,k):
        for j in range(2,k):
            Total_Prime = Total_Prime + 1
            Remainder = gcd(i,j)
            if Remainder==1:
                Relative_Prime = Relative_Prime + 1
    return Total_Prime/Relative_Prime
#Driver Code
k = int(input("Enter your number Please: "))
print("the probality of real prime numbers are: ", Real_Prime(k))