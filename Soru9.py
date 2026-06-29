class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_goster(self):
        print(f"{self.marka} {self.model} {self.yil}")

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya):
        Araba.__init__(self, marka, model, yil)
        self.batarya = batarya

    def sarjDurumu(self):
        print(f"Batarya: %{self.batarya}")

elektrikli = ElektrikliAraba("Tesla", "Model Y", 2026, 95)
elektrikli.bilgi_goster()
elektrikli.sarjDurumu()