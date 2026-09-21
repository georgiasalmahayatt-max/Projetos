# Calculadora de Consumo de Energia Elétrica

print("⚡ Calculadora de Consumo de Energia ⚡")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo opcional do custo mensal
valor_kwh = 0.75
custo_mensal = consumo_mensal * valor_kwh

print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}") 
