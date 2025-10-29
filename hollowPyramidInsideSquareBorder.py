n = 7
for i in range(n):
    for j in range(n):
        # Square border
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print('*', end=' ')
        # Hollow pyramid (top and bottom)
        elif i <= n // 2 and (j == n // 2 - i or j == n // 2 + i):
            print('*', end=' ')
        elif i > n // 2 and (j == i - n // 2 or j == n - 1 - (i - n // 2)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
