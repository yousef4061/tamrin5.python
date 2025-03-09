def chessboard(n, m):
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print("*", end='')
            else:
                print("#", end='')
        print()

n = int(input("adad ra vared kon: "))
m = int(input("adad ra vared kon: "))

chessboard(n, m)

#تمرین چاپ صفحه شطرنجی  