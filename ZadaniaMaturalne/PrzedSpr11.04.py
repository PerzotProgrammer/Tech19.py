input1 = input()
input2 = input()


# Palindrom
print("Palindrom (dla 1)")
if list(reversed(input1)) == list(input1):
    print(True)
else:
    print(False)

# Anagram
print("Anagram")
if sorted(input1) == sorted(input2):
    print(True)
else:
    print(False)



# Reszta
Nominaly = [500,200,100,50,20,10,5,2,1]
input1 = int(input())

while input1 > 0:
    for nominal in Nominaly:
        ile = input1 // nominal
        input1 -= ile * nominal
        print(f"Nominał {nominal} występuje {ile} razy")
