#!/usr/bin/env python3

# A beadott string karaktereit megnezi benne van e charsban es ha igen akkor csak azokat írja ki


def valid(text,chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    s = ""
    """Egyesével végig megy a text karakterein"""
    for e in text:
        """Megnézi benne van e a charsban"""
        if e in chars:
            s = s + e
    """Kiiratja"""
    print(s)



def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

if __name__ == "__main__":
    main()