#!/usr/bin/env python3

def main():
    try:
        a = int(input("Első szám: "))
        b = int(input("Második szám: "))
        print("Összeg: ",a + b)
    except ValueError:
        print("Nem lett magadva érték!")
        exit(1)

if __name__ == "__main__":
    main()