#!/usr/bin/env python3
# coding: utf-8


# kiyrja a sztringet normalizált állapotában
def normalize(s):
    return "".join(s.lower().split())


# Eldonti, hogy a megadott 2 sztring anagramma e
def anagram1(s1,s2):
    if sorted("".join(s1.lower().split())) == sorted("".join(s2.lower().split())):
        return True
    else:
        return False

def anagram2(s1,s2):
    li1 = list("".join(s1.lower().split()))
    li1.sort()
    li2 = list("".join(s2.lower().split()))
    li2.sort()

    return (li1 == li2)


def main():
    str1 = "Clint Eastwood"
    str2 = "Old west action"
    print(anagram1(str1, str2))
    print(anagram2(str1, str2))
    print(normalize("Old west action"))


if __name__ == "__main__":
    main()