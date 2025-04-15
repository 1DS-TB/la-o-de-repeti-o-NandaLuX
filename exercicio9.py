for num in range(1,10001):
  soma = 0
  for i in range(1, num):
    if num % i == 0:
        soma += i
  if soma == num:
      print(num)
