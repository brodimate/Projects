#!/usr/bin/env python3

import random

def main():
    szorzok = [1]
    n = 996300
    i = 2
    while i < 46:
        if n % i == 0:
            szorzok.append(i)
            n = n / i
        else:
            i += 1

    # valasszunk 6 random reszhalmazt a szorzok kozul
    # szorozzuk ossze a reszhalmazok elemeit hogy megkapjunk egy a lotton kihuzott szamot
    # folytassuk amig a kivalasztott 6 szam osszege nem lesz 90
    for s in range(10000):
        random.shuffle(szorzok)
        chunks_size = [1, 1, 1, 1, 1, 1]
        for i in range(5):
            chunks_size[random.choice(range(0, 5))] += 1
        starting_index = [sum(chunks_size[:i]) for i in range(len(chunks_size))]
        numbers = []
        for i, j in zip(starting_index, chunks_size):
            n = 1
            for k in szorzok[i:i+j]:
                n *= k
            numbers.append(n)
        if sorted(numbers)[-1] > 45 or len(set(numbers)) < 6:
            continue
        elif sum(numbers) == 90: 
            print(sorted(numbers))
            break

if __name__ == "__main__":
    main()
