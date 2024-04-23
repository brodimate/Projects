#!/usr/bin/env python3


# Kiírja, hogy a bekért sztring polindróm-e



def polindrom(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


def main():
    s = input("String: ")
    polindrom(s)


if __name__ == "__main__":
    main()