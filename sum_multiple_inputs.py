# Soma de Múltiplos Inputs - Projeto de Lógica de Programação

# Entrada: Quantidade de números a serem somados
n = int(input("Digite quantos números você deseja somar: "))

# Inicialização da soma
sum_total = 0

# Loop para ler os N números
for i in range(1, n + 1):
    value = float(input(f"Digite o {i}º número: "))
    sum_total += value

# Saída: Resultado da soma
print(f"A soma total é: {sum_total}")
