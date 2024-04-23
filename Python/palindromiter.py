#!/usr/bin/env python3

# megnézi, hogy a bekért szting polindróm-e

def main():
    s = input("String: ") 
    li = list(s) 
    ln = len(li) 
    rs = ""
    i = ln - 1 
    while i >= 0: 
        rs = rs + li[i] 
        i = i - 1 
    s = s.lower()
    rs = rs.lower() 

    if s == rs:
        print("Palindrome")
    else:
        print("Not palindrome")


if __name__ == "__main__":
    main()