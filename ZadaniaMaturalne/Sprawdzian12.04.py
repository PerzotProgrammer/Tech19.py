print("Zad1")
input1 = input("daj input: ")
input2 = input("daj input: ")

if input1 in input2:
    print(True)
else:
    print(False)

print("Zad2")

def IleJest(napis, co):
    ile = 0
    for i in range(len(napis)):
        if napis[i] == co:
            ile += 1
    return ile

input1 = input("daj input: ")

ileA = IleJest(input1, "a")
ileB = IleJest(input1, "b")
ileZ = IleJest(input1, "z")

if ileA >= 2 and ileB >= 1 and ileZ >= 1:
    print(True)
else:
    print(False)


print("zad3")
input1 = input("daj input: ")
print(list(input1))

def ZnajdzDup(napis):
    duplikaty = []
    maxNap = 0
    for i in napis:
        spr = napis.count(i)
        if spr > 1 and i not in duplikaty:
            duplikaty.append(True)
        else:
            duplikaty.append(False)
    return duplikaty

Duplikaty = ZnajdzDup(input1)
print(Duplikaty)

out = ""
powtorki = Duplikaty.count(True)
flaga = False
gdzie = 0

for i in range(powtorki):
    for i in range(len(input1)):
        if Duplikaty[i] == False:
            out += input1[i]
        elif Duplikaty[i] == True and flaga == False and gdzie != i:
            flaga = True
            out += input1[i]
            gdzie = i
    print(out)
    out = ""
    flaga = False