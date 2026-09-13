# 🔌 Calculadora de Consumo de Energia

Este projeto é uma calculadora simples que estima o consumo mensal de energia elétrica de um aparelho doméstico, com base na potência (em watts) e no tempo de uso diário.

## 📘 Como funciona

A calculadora utiliza a fórmula:

consumo_mensal = (potência_em_watts * horas_por_dia * 30) / 1000

O resultado é dado em kWh/mês, unidade usada pelas concessionárias de energia.

Também é calculado um custo estimado, usando um valor padrão de:

R$ 0,75 por kWh.

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Abra o terminal na pasta do projeto.
3. Execute:

   ```bash
   python app.py


3. O programa vai pedir:
   - Nome do aparelho
   - Potência (W)
   - Horas de uso por dia

---

## 📂 Estrutura do projeto

consumo-energia/
├── app.py  
└── README.md

---

## 👩‍💻 Autora

Projeto desenvolvido por **Georgia Salma Hayatt**.
