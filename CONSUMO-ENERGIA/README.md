# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-Consumo%20Elétrico-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📌 Sobre o projeto

A **Calculadora de Consumo de Energia** é um programa desenvolvido em Python com o objetivo de ajudar usuários a estimar o consumo mensal de energia elétrica de um aparelho.

O usuário informa o nome do aparelho, sua potência em watts (W) e o tempo médio de utilização diária. A partir dessas informações, o programa calcula o consumo estimado em **kWh por mês**.

Além disso, o sistema apresenta uma estimativa do custo mensal de utilização do aparelho, considerando o valor fixo de **R$ 0,75 por kWh**.

## 🐍 Tecnologia utilizada

O projeto foi desenvolvido utilizando:

* Python 3
* Git
* GitHub

## 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Onde:

* `potencia` = potência do aparelho em watts (W);
* `horasDia` = quantidade média de horas de uso por dia;
* `30` = quantidade estimada de dias no mês;
* `1000` = conversão de Wh para kWh.

Para calcular o custo estimado:

```text
custoMensal = consumoMensal × 0.75
```

## 💡 Exemplo

Para um aparelho de **1000 W**, utilizado durante **2 horas por dia**:

```text
consumoMensal = (1000 × 2 × 30) / 1000

consumoMensal = 60 kWh/mês
```

Considerando R$ 0,75 por kWh:

```text
custoMensal = 60 × 0.75

custoMensal = R$ 45,00
```

### Resultado

```text
⚡ Calculadora de Consumo de Energia ⚡

Digite o nome do aparelho: Ar-condicionado
Digite a potência do aparelho em watts (W): 1000
Digite o tempo médio de uso diário em horas: 2

--- Resultado ---
Aparelho: Ar-condicionado
Consumo estimado: 60.00 kWh/mês
Custo estimado: R$ 45.00
```

## ▶️ Como executar

Primeiro, certifique-se de que o **Python 3** esteja instalado no computador.

Clone o repositório:

```bash
git clone URL-DO-SEU-REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd consumo-energia
```

Execute o programa:

```bash
python app.py
```

## 📂 Estrutura do projeto

```text
consumo-energia/
│
├── app.py
└── README.md
```

## 🎯 Objetivo

Este projeto foi desenvolvido como atividade de iniciação em tecnologia, colocando em prática conceitos básicos de programação em Python, como:

* Entrada de dados;
* Variáveis;
* Operações matemáticas;
* Conversão de valores;
* Formatação de resultados;
* Uso de Git e GitHub;
* Documentação de projetos.

## ⚡ Economia de energia

Conhecer o consumo dos aparelhos elétricos ajuda a compreender melhor o uso da energia e pode auxiliar na adoção de hábitos mais conscientes.

---

⭐ **Projeto desenvolvido por Georgia Salma Hayatt para fins educacionais e de aprendizagem em Python.**
