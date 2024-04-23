#!/usr/bin/env python3

# Kiszámolja 2 pont távolságát

import math


def distance(p1, p2):
    d = math.sqrt((p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2)
    return d


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
