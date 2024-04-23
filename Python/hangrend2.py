#!/usr/bin/env python3

# Egy bekért szónak megmondja a hangrendjét
from enum import Enum, auto

class Direction(Enum):
    UP = 1

def mely(s):
    MELY_MGHK = "aáoóuú"
    count = 0
    for letter in s:
        if letter in MELY_MGHK:
            count += Direction.UP.value
    return (count)


def magas(s):
    MAGAS_MGHK = "eéiíöőüű"
    count = 0
    for letter in s:
        if letter in MAGAS_MGHK:
            count += Direction.UP.value
    return (count)


def main():
    word = input("Szó: ")
    mely(word)
    magas(word)
    if mely(word) != 0 and magas(word) == 0:
        print("Mély")
    elif mely(word) == 0 and magas(word) != 0:
        print("Magas")
    elif mely(word) != 0 and magas(word) != 0:
        print("Vegyes")
    else:
        print("Semmilyen")
    
            

#############################################################################

if __name__ == "__main__":
    main()
