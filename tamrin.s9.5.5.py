def multiplication_table(n, m):
    print(" ", end="")
    for j in range(1, m + 1):
        print(f"{j:4}", end="")
    print("\n" + "-" * (4 * m + 3))
    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for j in range(1, m + 1):
            print(f"{i * j:4}", end="")
        
        print()
n = int(input("adad ra vared kon: "))
m = int(input("adad ra vared kon: "))

multiplication_table(n, m)

# جدول اعداد ضرب