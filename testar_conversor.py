import unittest
from conversor import ConversordeMoedas

class TestConversordeMoedas(unittest.TestCase):

    def setUp(self):
        self.converter = ConversordeMoedas("proporcoes.json")

    def test_brl_para_usd(self):
        self.assertEqual(self.converter.convert(100, "BRL", "USD"), 19.0)

    def test_usd_para_brl(self):
        self.assertEqual(self.converter.convert(10, "USD", "BRL"), 53.5)

    def test_eur_para_usd(self):
        self.assertEqual(self.converter.convert(10, "EUR", "USD"), 11.7)

    def test_usd_para_eur(self):
        self.assertEqual(self.converter.convert(10, "USD", "EUR"), 8.5)

    def test_brl_para_jpy(self):
        self.assertEqual(self.converter.convert(1, "BRL", "JPY"), 27.97)

    def test_jpy_para_usd(self):
        self.assertEqual(self.converter.convert(1000, "JPY", "USD"), 6.7)

    def test_eur_para_brl(self):
        self.assertEqual(self.converter.convert(10, "EUR", "BRL"), 62.5)

    def test_brl_para_eur(self):
        self.assertEqual(self.converter.convert(100, "BRL", "EUR"), 16.0)

    def test_jpy_para_brl(self):
        self.assertEqual(self.converter.convert(100, "JPY", "BRL"), 3.6)

    def test_moeda_invalida(self):
        with self.assertRaises(ValueError):
            self.converter.convert(10, "ABC", "USD")

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-50, "USD", "BRL")

    def test_arrendondamento(self):
        self.assertEqual(self.converter.convert(1, "USD", "JPY"), 149.51)
        self.assertEqual(self.converter.convert(2, "USD", "JPY"), 299.02)
        self.assertEqual(self.converter.convert(0.123, "USD", "JPY"), round(0.123 * 149.51, 2))

if __name__ == "__main__":
    unittest.main()
