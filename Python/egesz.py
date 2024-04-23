#!/usr/bin/env python3


# kiírja a bekért szám fordítottját 


def egesz(s):
    print(s[::-1])
        


def main():
    s = input("Szám: ")
    egesz(s)


if __name__ == "__main__":
    main()