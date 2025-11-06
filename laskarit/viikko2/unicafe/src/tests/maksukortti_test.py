import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luonti_onnistuu(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alku_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroissa(), 35.0)

    def test_negatiivinen_rahan_lataus_ei_muuta_saldoa(self):
        self.maksukortti.lataa_rahaa(-500)

        self.assertEqual(self.maksukortti.saldo_euroissa(), 10.0)

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroissa(), 5.0)

    def test_rahan_ottaminen_liikaa_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroissa(), 10.0)

    def test_rahan_ottaminen_palauttaa_true(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_rahan_ottaminen_liikaa_palauttaa_false(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1500))
