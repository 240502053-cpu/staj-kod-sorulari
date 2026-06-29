sayilar = [15, 3, 7, 20, 8, 11]

en_buyuk = sayilar[0]
en_kucuk = sayilar[0]

for sayi in sayilar:

    if sayi > en_buyuk:
        en_buyuk = sayi

    if sayi < en_kucuk:
        en_kucuk = sayi

print("En büyük sayı:", en_buyuk)
print("En küçük sayı:", en_kucuk)