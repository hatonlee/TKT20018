class Maksukortti:
    def __init__(self, saldo):
        self.saldo = saldo

    def lataa_rahaa(self, maara):
        if maara > 0:
            self.saldo += maara

    def ota_rahaa(self, maara):
        if self.saldo < maara:
            return False

        self.saldo = self.saldo - maara
        return True

    def saldo_euroissa(self):
        return self.saldo / 100

    def __str__(self):
        saldo_euro = self.saldo_euroissa()
        return f"Kortilla on rahaa {saldo_euro:0.2f} euroa"
