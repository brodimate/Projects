#!/usr/bin/env python3


# Kiírja, hogy a bekért sztring polindróm-e



def polindrom(s):
    if s == s[::-1]:
        print("A bekért szöveg polindróm")
    else:
        print("A bekért szöveg nem polindróm")


def main():
    s = input("Vizsgálandó szöveg: ")
    polindrom(s)


if __name__ == "__main__":
    main()