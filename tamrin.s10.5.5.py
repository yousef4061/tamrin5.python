def print_diamond(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)
    
n = int(input("(adad fard)andazeh lozi ra vared kon: "))
if n % 2 == 0:
    n += 1
print_diamond(n)