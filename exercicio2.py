num = int(input("Digite um número: "))
soma = 0
contador = 1

while contador <= num:
  soma = soma + contador
  contador = contador + 1

print(f"A soma dos números de 1 a {num} é: {soma}")