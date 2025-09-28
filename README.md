# Conversor de Moedas

## Descrição do Projeto
O **Conversor de Moedas** é um sistema simples em Python que permite converter valores entre diferentes moedas usando **taxas de câmbio pré-definidas**.  
O projeto inclui uma interface de linha de comando amigável para o usuário e testes unitários que garantem que a funcionalidade está correta e precisa.

Link para Quadro no Trello: https://trello.com/invite/b/68d94a052df79f23dc348dbb/ATTI84398b6552030eaabf8efa2cb83d40594D584B5F/agile-docs-code-sprint

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

1. **Instalar o Python (se ainda não estiver instalado)**  
   - Acesse o site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
   - Baixe a versão mais recente compatível com seu sistema operacional (recomenda-se Python 3.10 ou superior)  
   - Durante a instalação, marque a opção **"Add Python to PATH"** para poder usar o Python no terminal/Prompt de Comando

2. Clone o repositório:
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
Obs: Dados coletados do **Google Finanças** em 28/09/2025

## Como Rodar os Testes Unitários

Os testes foram escritos usando o framework unittest. Eles verificam:

- Precisão das conversões

- Arredondamento correto

- Tratamento de entradas inválidas (moeda não suportada, valores negativos)

Para executar os testes:

```bash
python -m unittest testar_conversor.py
```

## Critérios de Aceitação

O conversor cumpre os seguintes critérios:

- Permite selecionar moeda de origem e destino

- Permite inserir valor a ser convertido

- Exibe o valor convertido corretamente com 2 casas decimais

- Valida entradas inválidas e valores negativos

- Testes unitários cobrem todos os cenários positivos e negativos

## Futuras Melhorias

- Integração com API de câmbio em tempo real

- Interface gráfica (GUI) para maior usabilidade

- Armazenamento de histórico de conversões

- Suporte a mais moedas internacionais
