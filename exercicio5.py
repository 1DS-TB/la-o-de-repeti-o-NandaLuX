num = int(input("Digite um número: "))

if num <= 1:

  for i in range(2, num):
    if num % i == 0:
      print("Não é um número primo!")
  print("Não é um número primo!")

else:
  print("É um número primo!")