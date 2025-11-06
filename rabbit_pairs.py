#Recurrence relation
def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)
print(rabbit_pairs(36, 4)) #Example pair of (n,k)
