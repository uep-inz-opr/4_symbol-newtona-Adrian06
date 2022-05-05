import math as mt

n, k = input().split()
n = int(n)
k = int(k)

newton_symbol = (mt.factorial(n))//(mt.factorial(k)*mt.factorial(n-k))
print(newton_symbol)