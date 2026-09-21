# 🛒 Sistema de Desconto Progressivo

## 📌 Sobre o projeto

Este projeto foi desenvolvido em **Python** com o objetivo de implementar um sistema de desconto progressivo para uma loja online.

O programa solicita ao usuário o valor total da compra, identifica automaticamente o percentual de desconto correspondente e apresenta o valor do desconto e o valor final que deverá ser pago pelo cliente.

## 💰 Regras de desconto

O sistema utiliza as seguintes regras:

* Compras abaixo de **R$ 200,00** recebem **5% de desconto**.
* Compras a partir de **R$ 200,00** e abaixo de **R$ 300,00** recebem **10% de desconto**.
* Compras a partir de **R$ 300,00** recebem **15% de desconto**.

## ⚙️ Como funciona

O usuário informa o valor total da compra.

Em seguida, o programa:

1. Verifica em qual faixa de desconto a compra se encontra.
2. Calcula o percentual de desconto correspondente.
3. Calcula o valor do desconto.
4. Calcula o valor final da compra.
5. Exibe os resultados na tela.

## 🧪 Exemplo de execução

```text
Digite o valor total da compra: R$ 300

--- RESUMO DA COMPRA ---
Valor da compra: R$ 300.00
Desconto aplicado: 15%
Valor do desconto: R$ 45.00
Valor total a pagar: R$ 255.00
```

## 🐍 Tecnologias utilizadas

* Python
* Estruturas condicionais (`if`, `elif` e `else`)
* Entrada de dados com `input()`
* Conversão de dados com `float()`
* Operações matemáticas
* Formatação de valores

## 📂 Estrutura do projeto

```text
desconto-progressivo/
│
├── app.py
└── README.md
```

## ▶️ Como executar

Para executar o programa, abra o terminal na pasta do projeto e utilize:

```bash
python app.py
```

Depois, informe o valor total da compra solicitado pelo programa.

## 🎯 Objetivo da atividade

Praticar os conceitos básicos da linguagem Python, principalmente:

* Entrada e saída de dados;
* Variáveis;
* Operadores matemáticos;
* Estruturas condicionais;
* Cálculo de porcentagens.

## 👩‍💻 Autora

Projeto desenvolvido por Georgia Salma Hayatt para atividade prática de programação em **Python**.
