import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_lataa_rahaa_toimii(self):
        kortti = Maksukortti(10)
        
        kortti.lataa_rahaa(10)

        self.assertEqual(str(kortti), "saldo: 0.2")

    def test_ota_rahaa_toimii(self):
        kortti = Maksukortti(10)

        kortti.ota_rahaa(5)

        self.assertEqual(str(kortti), "saldo: 0.05")

    def test_ota_rahaa_ei_toimi(self):
        kortti = Maksukortti(10)

        kortti.ota_rahaa(15)

        self.assertEqual(str(kortti), "saldo: 0.1")

    def test_nayta_saldo(self):
        kortti = Maksukortti(10)

        kortti.__str__()

        self.assertEqual(str(kortti), "saldo: 0.1")