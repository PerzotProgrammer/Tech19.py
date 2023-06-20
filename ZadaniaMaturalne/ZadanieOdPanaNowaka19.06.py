from random import randint

T = [randint(-10, 10) for i in range(10)]

# T = [1, -2, -4, 6, -4]


print(T)

maxAktualny = 0
maxNajlepszy = 0

for liczba in T:
	maxAktualny = max(liczba, maxAktualny + liczba)
	maxNajlepszy = max(maxNajlepszy, maxAktualny)
print(maxNajlepszy)

