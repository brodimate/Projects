#!/usr/bin/env python3

#Kirajzol egy h1 magasságú gyémántot ahol h1 csak páratlan lehet

import sys



def main():
    h1 = int(input("Diamond height: "))
    h2 = int(h1/2 + 1)
    if (h1%2):
        for eu in range(1,h2+1):
            print(" " * (h2 - eu) + "*" * ((eu*2)-1))
        for ed in range(h2-1):
            print(" " * (ed+1) + "*" * (((h2*2)-3) - ed*2))
    else:
        print("Csak páratlan számot adhatunk meg!")
    

#############################################################################

if __name__ == "__main__":
    main()
