# 💧 Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Água](https://img.shields.io/badge/Consumo-Água-00BFFF)
![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-♻️-green)

## 📌 Sobre o projeto

O **Sistema de Classificação de Consumo de Água** foi desenvolvido em Python com o objetivo de classificar o perfil de consumo de água de diferentes tipos de imóveis e emitir alertas educativos aos moradores.

O projeto faz parte de uma proposta de conscientização ambiental, incentivando o consumo responsável de água e ajudando a identificar situações de consumo econômico, moderado ou excessivo.

## 🎯 Objetivo

O programa solicita ao usuário:

* 🏠 O tipo de imóvel: **comercial, casa ou apartamento**;
* 💧 O consumo mensal de água em metros cúbicos (**m³**).

Com essas informações, o sistema analisa o consumo e apresenta uma mensagem de acordo com as regras estabelecidas.

## 📋 Regras de classificação

### 🏢 Imóvel comercial

Para imóveis do tipo **comercial**, o sistema apresenta:

> Tarifa comercial aplicada – consulte o plano corporativo.

### 🏬 Apartamento com consumo menor que 10 m³

O sistema apresenta:

> Consumo econômico – excelente controle de água!

### 🏡 Casa ou apartamento com consumo de até 25 m³

O sistema apresenta:

> Consumo moderado – dentro do padrão residencial.

### ⚠️ Consumo acima do limite residencial

Nos demais casos, o sistema apresenta:

> Consumo excessivo – adote medidas de economia e verifique vazamentos.

## 🧪 Exemplo utilizado

Para demonstrar o funcionamento do programa, foi utilizado um **apartamento com consumo mensal de 5 m³**.

Como o consumo é menor que **10 m³**, ele é classificado como **consumo econômico**.

```text
Digite o tipo de imóvel (comercial, casa ou apartamento): apartamento
Digite o consumo mensal de água em m³: 5

Consumo econômico – excelente controle de água!
```

## 🐍 Tecnologia utilizada

O projeto foi desenvolvido utilizando:

* 🐍 **Python**
* 💻 **Visual Studio Code**
* 🐙 **GitHub**
* ♻️ Conceitos de sustentabilidade e consumo consciente

## ▶️ Como executar o programa

1. Baixe ou clone este repositório.
2. Abra a pasta `consumo-agua` no Visual Studio Code.
3. Certifique-se de que o Python está instalado no computador.
4. Abra o terminal na pasta do projeto.
5. Execute o comando:

```bash
python app.py
```

6. Informe o tipo de imóvel.
7. Digite o consumo mensal de água em metros cúbicos.
8. O programa apresentará automaticamente a classificação do consumo.

## 📂 Estrutura do projeto

```text
consumo-agua/
├── app.py
└── README.md
```

## 💻 Código principal

O arquivo `app.py` utiliza estruturas condicionais para realizar a classificação do consumo.

```python
tipo_imovel = input(
    "Digite o tipo de imóvel (comercial, casa ou apartamento): "
).lower()

consumo = float(
    input("Digite o consumo mensal de água em m³: ")
)

if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
```

## 📚 Conceitos aplicados

Durante o desenvolvimento foram utilizados conceitos fundamentais de Python:

* Entrada de dados com `input()`;
* Conversão de valores com `float()`;
* Estruturas condicionais `if`, `elif` e `else`;
* Operadores relacionais;
* Operadores lógicos `and` e `or`;
* Manipulação de strings com `.lower()`.

## 🌱 Sustentabilidade

O consumo consciente de água é fundamental para a preservação dos recursos naturais.

Neste exemplo, o apartamento apresenta um consumo mensal de **5 m³**, sendo classificado pelo sistema como **consumo econômico**. 💧✅

---

### 💧 Economizar água é preservar o futuro! 🌎♻️

**Desenvolvido por Georgia Salma Hayatt com Python 🐍 e foco em sustentabilidade.**
