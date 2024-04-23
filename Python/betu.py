#!/usr/bin/env python3


# A program bekért egy szöveget amiről megállapítja, hogy csak kisbetűből áll-e vagy van-e benne legalább egy nagybetű is.


def meret(s):
    if s.islower() == True:
        print("A bekért szöveg csak kisbetűből áll")
    else:
        print("A bekért szövegben van legalább egy nagybetű")


def main():
    s = input("kiértékelendő szöveg: ")
    meret(s)


if __name__ == "__main__":
    main()
