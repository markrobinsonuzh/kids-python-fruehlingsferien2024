imput = input("pick random number from 1 to 20")
imput = int(imput)
print(type(imput))
for i in range(1, 13):
    print(str(imput) + "x" + str(i) + "=" + str(i * imput))

