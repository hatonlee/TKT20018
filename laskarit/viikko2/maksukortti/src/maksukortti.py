EDULLINEN = 250
MAUKAS = 400


class Maksukortti:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def syo_edullisesti(self):
        if self.saldo >= EDULLINEN:
            self.saldo -= EDULLINEN

    def syo_maukkaasti(self):
        if self.saldo >= MAUKAS:
            self.saldo -= MAUKAS

    def lataa_rahaa(self, maara):
        if maara < 0:
            return

        self.saldo += maara
        self.saldo = min(self.saldo, 15000)

    def saldo_euroina(self):
        return self.saldo / 100

    def __str__(self):
        saldo_euro = self.saldo_euroina()
        return f"Saldo: {saldo_euro:0.2f} euroa"
