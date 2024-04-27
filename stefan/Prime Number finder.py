

notprime = []
prime = [2]


for number in range(3,201):
  count = 0
  for p in prime:
    print(number, p, count)
    if number % p  == 0 :
      notprime.append(number)
    else : 
      count = count + 1
    if count == len(prime):
      prime.append(number)
print("prime")
print(prime)
