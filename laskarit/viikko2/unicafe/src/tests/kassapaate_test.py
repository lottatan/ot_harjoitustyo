import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullisesti_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullisesti_ei_toimi(self):
        tulos = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(tulos, 200)

    def test_kateisosto_maukkaasti_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukkaasti_ei_toimi(self):
        tulos =  self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(tulos, 300)


    def test_korttiosto_edullisesti_toimii(self):
        maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(tulos, True)

    def test_korttiosto_edullisesti_ei_toimi(self):
        maksukortti = Maksukortti(200)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(tulos, False)

    def test_korttiosto_maukkaasti_toimii(self):
        maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(tulos, True)

    def test_korttiosto_maukkaasti_ei_toimi(self):
        maksukortti = Maksukortti(300)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo, 300)
        self.assertEqual(tulos, False)

    def test_kortin_lataus_toimii(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(maksukortti.saldo, 1100)

    def test_kortin_lataus_ei_toimi(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -10)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksukortti.saldo, 1000)