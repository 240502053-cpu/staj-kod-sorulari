def asal_mi(sayi):

    if sayi <= 1:
        return False

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False

    return True

print("1-100 Arasındaki Asal Sayılar:")
for x in range(1, 101):
    if asal_mi(x):
        print(x, end=" ")
print()