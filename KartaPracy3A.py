x = 10
#zad1
print("ZADANIE 1")
for i in range(1, x):
    print("*-|",end = "")
print("")

#zad2
print("ZADANIE 2")
gw = "*"
kr = "--"
pi = "||"
for i in range (1, x):
    print(gw + kr + gw + "*" + pi, end="")
    gw = gw + "**"
