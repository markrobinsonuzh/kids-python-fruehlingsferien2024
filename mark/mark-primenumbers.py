
notprime=[]
prime=[2]

for i in range(3, 200):
  count = 0
  for p in prime: 
    if i%p == 0:
      notprime.append(i)
      break
    else:
      count=count+1
  # print(i, p, count, len(prime))
  if count==len(prime):
       prime.append(i)

print("Prime numbers:")
print(prime)
print("Non-prime numbers:")
print(notprime)
