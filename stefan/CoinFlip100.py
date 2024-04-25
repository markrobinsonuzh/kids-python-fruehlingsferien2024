import numpy as np
import random as rd


count = 0

for i in range(0,100):
  flip = rd.choices(["Head","Tail"])
  print(str(i), str(flip))
  if(flip[0]=="Head"):
    count = count + 1
  
  
    
print(count)
