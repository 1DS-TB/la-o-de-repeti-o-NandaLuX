n = int(input("Digite um número: "))
soma = 0

for i in range(1, n+1):
  soma += i / 1
  print(f"Soma da séria harmônica até {n} termos: {soma:.2f}")