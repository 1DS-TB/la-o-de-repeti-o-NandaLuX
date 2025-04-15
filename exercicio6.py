num = int(input("Digite um número para a sequência desejada: "))
a = 0
b = 1

for i in range(num):
  print(a)
  a, b = b, a + b
