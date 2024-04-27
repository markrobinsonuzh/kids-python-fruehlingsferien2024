import numpy as np

for number in range(3000,7000):
  ungerade = number % 2 != 0
  number_str = str(number)
  number_split = [x for x in number_str]
  count = 0
  for i in number_split : 
    count = count + int(i)
  y = np.unique(number_split)
  if len(number_split) == len(y) and number % 2 != 0 and number % 5 == 0 and count == 23 :
    print(number)
