import json

class ConversordeMoedas:
    def __init__(self, rates_file="proporcoes.json"):
        with open(rates_file, "r", encoding="utf-8") as file:
            self.rates = json.load(file)

    def convert(self, valor: float, moeda_origem: str, moeda_convertida: str) -> float:
        """Converte um valor de uma moeda para outra, se possível."""
        moeda_origem = moeda_origem.upper()
        moeda_convertida = moeda_convertida.upper()

        if moeda_origem not in self.rates:
            raise ValueError(f"Moeda de origem '{moeda_origem}' não suportada.")
        if moeda_convertida not in self.rates.get(moeda_origem, {}):
            raise ValueError(f"Conversão de {moeda_origem} para {moeda_convertida} não suportada.")
        if valor < 0:
            raise ValueError("O valor a ser convertido não pode ser negativo.")

        rate = self.rates[moeda_origem][moeda_convertida]
        return round(valor * rate, 2)


def main():
    converter = ConversordeMoedas()

    print("=== Conversor de Moedas ===")
    print("Moedas disponíveis: BRL, USD, EUR, JPY")

    moeda_origem = input("Digite a moeda de origem: ").strip().upper()
    moeda_convertida = input("Digite a moeda de destino: ").strip().upper()
    valor = float(input("Digite o valor a ser convertido: "))

    try:
        result = converter.convert(valor, moeda_origem, moeda_convertida)
        print(f"{valor} {moeda_origem} equivalem a {result} {moeda_convertida}")
    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
