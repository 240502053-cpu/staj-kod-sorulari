class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0.0):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n[+] İşlem Başarılı: {miktar} TL yatırıldı.")
            self.bakiye_goster()
        else:
            print("\n[!] Hata: Yatırılacak miktar 0'dan büyük olmalıdır!")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("\n[!] Hata: Çekilecek miktar geçersiz!")
        elif miktar > self.bakiye:
            print(f"\n[!] Hata: Yetersiz bakiye! Mevcut bakiyeniz: {self.bakiye} TL")
        else:
            self.bakiye -= miktar
            print(f"\n[-] İşlem Başarılı: {miktar} TL çekildi.")
            self.bakiye_goster()

    def bakiye_goster(self):
        print(f"[*] Sayın {self.hesap_sahibi}, Güncel Bakiyeniz: {self.bakiye} TL")

isim = input("Lütfen adınızı ve soyadınızı giriniz: ")
hesap = BankaHesabi(isim, 1000.0)
print(f"\nHos geldiniz {isim}! Hesabınız 1000 TL bakiye ile açıldı.")

while True:
    print("\n" + "=" * 30)
    print("      BANKAMATİK MENÜSÜ      ")
    print("=" * 30)
    print("1 - Bakiye Sorgula")
    print("2 - Para Yatır")
    print("3 - Para Çek")
    print("4 - Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemin numarasını girin: ")

    if secim == "1":
        print()
        hesap.bakiye_goster()

    elif secim == "2":
        try:
            miktar = float(input("\nYatırmak istediğiniz tutarı girin: "))
            hesap.para_yatir(miktar)
        except ValueError:
            print("\n[!] Hata: Lütfen sadece sayısal bir değer giriniz!")

    elif secim == "3":
        try:
            miktar = float(input("\nÇekmek istediğiniz tutarı girin: "))
            hesap.para_cek(miktar)
        except ValueError:
            print("\n[!] Hata: Lütfen sadece sayısal bir değer giriniz!")

    elif secim == "4":
        print(f"\nBizi tercih ettiğiniz için teşekkür ederiz, iyi günler {isim}!")
        break
    else:
        print("\n[!] Geçersiz seçim! Lütfen 1, 2, 3 veya 4 yazınız.")