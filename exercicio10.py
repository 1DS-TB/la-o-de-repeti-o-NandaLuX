num1 = int(input("Digite o número do início: "))
num2 = int(input("Digite o número do fim: "))

print(f"O intervalo de {num1} e {num2} é: ")

for num in range(num1, num2+1):
  conta = str(num ** 2)
  for i in range(1, len(conta)):
    parte1 = conta[:i]
    parte2 = conta[i:]
    if parte2 == 0:
      continue
    if int(parte1) + int(parte2) == num:
      print(num)
      break