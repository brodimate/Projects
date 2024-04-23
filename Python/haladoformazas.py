#!/usr/bin/env python3

# Bekér neveket és a hozzá tartozó korokat majd formázva kiíratja

def main():
    a1 = input("Név: ")
    a2 = int(input("Kor: "))
    a3 = input("Név: ")
    a4 = int(input("Kor: "))
    tabla = [
        [a1, a2],
        [a3, a4],
    ]


    sor = ("| {nev:<20s} | {kor:5d}|").format

    for s in tabla:
        print(sor(nev=s[0], kor=s[1]))


if __name__ == "__main__":
    main()