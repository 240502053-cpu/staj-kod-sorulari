class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_goster(self):
        print(f"{self.marka} {self.model} {self.yil}")


araba1 = Araba("Volkswagen", "Passat", 2020)
araba1.bilgi_goster()