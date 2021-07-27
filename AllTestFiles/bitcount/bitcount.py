
def bitcount(n):
    count = 0
    while n:
        n = n - 1 #from ^= to =
        count += 1
    return count
