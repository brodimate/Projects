#!/usr/bin/env python3

# kizaró vagy

def main():
    str1 = input("String1 in: ")
    str2 = input("String2 in: ")
    if bool(str1) == True and bool(str2) == False or bool(str1) == False and bool(str2) == True:
        print("Teljesül")
    else:
        print("Nem teljesül")



if __name__ == "__main__":
    main()