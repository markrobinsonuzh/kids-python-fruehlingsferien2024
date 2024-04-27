

notprime = []
prime = [2]


for i in range(3, 200):
  count = 0
  for p in prime:
    if i%p == 0:
       notprime.append(i)
    else:
       count=count+1

  if count==len(prime):
      prime.append(i)
print(prime)


