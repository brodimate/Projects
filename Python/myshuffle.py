#!/usr/bin/env python3

import random


def shuffled(li):
    copy = li[:]
    random.shuffle(copy)
    return copy



def main():
    li = [1, 2, 3, 4, 5]
    uj = shuffled(li)[-1]
    print(uj)


if __name__ == "__main__":
    main()