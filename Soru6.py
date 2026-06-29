ogrenciler = [
    ["Sude", 100],
    ["Ayşe", 90],
    ["Ecmel", 55],
    ["Zeynep", 80]
]

notlar = [ogrenci[1] for ogrenci in ogrenciler]

ortalama = sum(notlar) / len(ogrenciler)

en_yuksek_not = max(notlar)
en_yuksek_ogrenci = ogrenciler[notlar.index(en_yuksek_not)][0]

kalanlar = [ogrenci[0] for ogrenci in ogrenciler if ogrenci[1] < 60]

print(f"--- ÖĞRENCİ NOT SİSTEMİ RAPORU ---")
print(f"Sınıf Ortalaması: {ortalama}")
print(f"En Yüksek Notu Alan Öğrenci: {en_yuksek_ogrenci} ({en_yuksek_not})")
print(f"Kalan Öğrenciler (60 Altı): {kalanlar}")