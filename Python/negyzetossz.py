#!/usr/bin/env python3

# kiírja a 1-től 100-ig a számok negyzetösszegét

def negyzetosszeg(num1):
    negyzetösszeg = 0
    for n1 in num1:
        negyzetösszeg += n1*n1
    return negyzetösszeg

# kiírja 1-től 100-ig a számok összegének a négyzetét

def osszegnegyzet(num2):
    osszegnegyzet = 0
    for n2 in num2:
        osszegnegyzet += n2
    return osszegnegyzet ** 2

def main():
    tsz = range(1,100 + 1)
    kulonbseg = osszegnegyzet(tsz) - negyzetosszeg(tsz)
    print(kulonbseg) 
    

    

#############################################################################

if __name__ == "__main__":
    main()
