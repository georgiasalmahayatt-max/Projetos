# 📊 Pesquisa de Opinião — TudoWeb

## 📝 Sobre o projeto

Este projeto foi desenvolvido em **Python** com o objetivo de realizar uma pesquisa de opinião sobre o atendimento prestado pela empresa **TudoWeb**.

O programa coleta os dados dos entrevistados e registra a avaliação do atendimento, permitindo contabilizar ao final da pesquisa a quantidade de respostas **EXCELENTE** e **RUIM**.

---

## 🎯 Objetivo

Desenvolver um programa utilizando **estruturas de repetição** e **estruturas de decisão** para coletar e analisar as respostas de uma pesquisa de satisfação.

Cada entrevistado deve informar:

* 👤 Nome
* 🎂 Idade
* ⭐ Opinião sobre o atendimento

As opções disponíveis são:

* `1` — EXCELENTE
* `2` — BOM
* `3` — RUIM

---

## 🔄 Funcionamento

O programa utiliza a estrutura de repetição `for` para realizar a pesquisa com os entrevistados.

Para verificar cada resposta, são utilizadas as estruturas condicionais:

* `if`
* `elif`
* `else`

Ao final da pesquisa, o programa apresenta:

* Quantidade de respostas **EXCELENTE**
* Quantidade de respostas **RUIM**

---

## 🧪 Teste do programa

Para validar o funcionamento do programa, foram realizados testes considerando **10 entrevistados**.

Exemplo de respostas:

| Entrevistado | Opinião   |
| ------------ | --------- |
| 1            | EXCELENTE |
| 2            | BOM       |
| 3            | EXCELENTE |
| 4            | RUIM      |
| 5            | BOM       |
| 6            | EXCELENTE |
| 7            | BOM       |
| 8            | RUIM      |
| 9            | EXCELENTE |
| 10           | BOM       |

### 📌 Resultado esperado

```text
=== RESULTADO DA PESQUISA ===
Quantidade de respostas EXCELENTE: 4
Quantidade de respostas RUIM: 2
```

---

## 💻 Código utilizado

```python
excelente = 0
ruim = 0

print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")

for entrevistado in range(1, 11):
    print(f"\nEntrevistado {entrevistado}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nAvalie o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opinião inválida!")

print("\n=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
```

---

## 👥 Versão final — 50 entrevistados

Após os testes com 10 entrevistados, o programa pode ser configurado para realizar a pesquisa com **50 pessoas**.

Para isso, basta alterar:

```python
for entrevistado in range(1, 11):
```

para:

```python
for entrevistado in range(1, 51):
```

Dessa forma, o programa executará a pesquisa para os **50 entrevistados**, conforme solicitado na atividade.

---

## ▶️ Como executar

1. Tenha o **Python** instalado no computador.
2. Abra a pasta do projeto no **Visual Studio Code**.
3. Abra o terminal.
4. Execute:

```bash
python app.py
```

5. Informe o nome, a idade e a opinião de cada entrevistado.
6. Ao finalizar a pesquisa, o resultado será apresentado na tela.

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 💻 Visual Studio Code
* 🐙 Git
* 🌐 GitHub

---

## 📚 Conceitos utilizados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

* Variáveis
* Entrada de dados com `input()`
* Conversão de dados com `int()`
* Estrutura de repetição `for`
* Estruturas condicionais `if`, `elif` e `else`
* Contadores
* Operadores de comparação
* Saída de dados com `print()`

---

## 👩‍💻 Autora

Desenvolvido por **Georgia Salma Hayatt** como atividade prática de programação em Python.
