num = int(input("Digite um número: "))
fatorial = 1
contador = ""

for i in range(num, 0, -1):
  fatorial = fatorial + i
  if i == 1:
    contador += f"{i}"
  else:
    contador += f"{i} x "

print(f"{num}! = {contador} = {fatorial}")