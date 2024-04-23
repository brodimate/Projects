#!/usr/bin/env python3

# Kiirja az abc-t vagy forditva attól függően, hogy melyik szmbolikus linkkel osszekotott scriptet futtatjuk

import sys

def main():
    """A parancssori argumentumokbol alapján megézi melyik scriptet futattuk"""
    if sys.argv[0] == "./a-z.py":
        print("abcdefghijklmnopqrstuvwxyz")
        """Ha az a-z.py-t akkor kiirja az abc-t
        
        Ha nem azt akkor kiirja a fordított abc-t"""
    else:
        print("zyxwvutsrqponmlkjihgfedcba")


if __name__ == "__main__":
    main()