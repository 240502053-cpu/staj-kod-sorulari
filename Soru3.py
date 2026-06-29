kelime = input("Bir kelime giriniz: ")

ters_kelime = ""

for harf in kelime:
    ters_kelime = harf + ters_kelime

print("Kelimenin tersi:", ters_kelime)