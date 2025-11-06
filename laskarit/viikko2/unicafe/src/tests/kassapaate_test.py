import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_alku_saldo(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_alku_myyty(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_osto_veloitus(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihto, 500 - 240)

    def test_edullinen_osto_epaonnistuu(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihto, 200)

    def test_edullinen_osto_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_osto_epaonnistuu_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_osto_veloitus(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 500 - 400)

    def test_maukas_osto_epaonnistuu(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihto, 200)

    def test_maukas_osto_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_osto_epaonnistuu_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_edullinen_osto_kortilla_onnistuu(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(tulos)

    def test_edullinen_osto_kortilla_myydyt(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_osto_kortilla_epaonnistuu(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertFalse(tulos)

    def test_edullinen_osto_kortilla_epaonnistuu_myydyt(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_maukas_osto_kortilla_onnistuu(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(tulos)

    def test_maukas_osto_kortilla_myydyt(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_osto_kortilla_epaonnistuu(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertFalse(tulos)

    def test_maukas_osto_kortilla_epaonnistuu_myydyt(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_lataus_kortilla_kassa_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0 + 1.0)

    def test_lataus_kortilla_epaonnistuu_kassa_raha(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
