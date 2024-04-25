
# Mark test example of Fibonacci sequence

x1 = 0
x2 = 1

print(x1)
print(x2)

for i in range(0,19):
  next_val = x1 + x2
  print(str(i) + ": " + str(next_val))
  x1 = x2
  x2 = next_val
  
  
  
