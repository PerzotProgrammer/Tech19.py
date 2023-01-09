# KODOWANIE HASHOWE
from hashlib import md5, sha256, sha512
input1 = input()

print(sha512(input1.encode("utf-8")).hexdigest())

# W PĘTLI
for i in range(10000):
    print(sha512(str(i).encode("utf-8")).hexdigest())
