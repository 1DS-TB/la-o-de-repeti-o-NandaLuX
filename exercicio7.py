n = int(input("Digite um número: "))

for i in range(1, 1+n):
  for num in range(1, i+1):
    print("*", end="")
  print()