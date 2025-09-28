# Conversor de Moedas

## Descrição do Projeto
O **Conversor de Moedas** é um sistema simples em Python que permite converter valores entre diferentes moedas usando **taxas de câmbio pré-definidas**.  
O projeto inclui uma interface de linha de comando amigável para o usuário e testes unitários que garantem que a funcionalidade está correta e precisa.

### Moedas suportadas
- BRL (Real Brasileiro)  
- USD (Dólar Americano)  
- EUR (Euro)  
- JPY (Iene Japonês)

---

## Estrutura do Projeto
```yaml
currency_converter/
│
├── converter.py # Código principal do conversor
├── proporcoes.json # Taxas de câmbio pré-definidas
├── testar_conversor.py # Testes unitários
└── README.md # Documentação do projeto
```

---

## Como Executar o Conversor

1. Clone o repositório:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd currency_converter
```
Execute o conversor:
```bash
python converter.py
```
Siga as instruções no terminal:

Digite a moeda de origem (ex: BRL)

Digite a moeda de destino (ex: USD)

Digite o valor a ser convertido (ex: 100)

O programa retornará o valor convertido com 2 casas decimais, por exemplo:

```css
100 BRL equivalem a 19.0 USD
```
## Taxas de Conversão Utilizadas

As taxas estão armazenadas em proporcoes.json:

```json
{
  "BRL": {"USD": 0.19, "JPY": 27.97, "EUR": 0.16},
  "USD": {"BRL": 5.35, "EUR": 0.85, "JPY": 149.51},
  "EUR": {"USD": 1.17, "JPY": 175.16, "BRL": 6.25},
  "JPY": {"USD": 0.0067, "EUR": 0.0057, "BRL": 0.036}
}
```

## Como Rodar os Testes Unitários

Os testes foram escritos usando o framework unittest. Eles verificam:

- Precisão das conversões

- Arredondamento correto

- Tratamento de entradas inválidas (moeda não suportada, valores negativos)

Para executar os testes:

```bash
python -m unittest testar_conversor.py
```
