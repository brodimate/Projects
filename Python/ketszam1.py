#!/usr/bin/env python3

import sys



def main():
    if len(sys.argv) > 2:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print("Összeg: ",a + b)
        except ValueError:
            print("Nem csak számok lettek megadva!")
            exit(1)
    else:
        print("Nincs megadva elég argumentum!")

if __name__ == "__main__":
    main()