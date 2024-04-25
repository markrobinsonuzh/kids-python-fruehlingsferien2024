
input_string = input("Enter a string: ")
print(input_string)

x = input_string
print(x)
print(x[::-1])

if(x==x[::-1]):
  print("Yes, your string is a palindrome")
else:
  print("No, your string is not a palindrome")
  
  
