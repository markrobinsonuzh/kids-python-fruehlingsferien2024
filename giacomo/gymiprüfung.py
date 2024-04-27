import numpy as np

for number in range(3000, 7000):
  ungerade = number % 2 != 0
  string = str(number)
  letter = [x for x in string]
  count = 0
  for i in letter:
    count = count + int(i)
  #print(number, count)
  y = np.unique(letter)
  if len(letter) == len(y) and number % 2 != 0 and count == 23 and number % 5 == 0:
    print(number)
  
  
  
