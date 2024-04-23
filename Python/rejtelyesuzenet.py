#!/usr/bin/env python3

# A program kiirja a szöveg megfejtését (eltolja a betűket 2-vel az abc-ben)

TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

alphabet="abcdefghijklmnopqrstuvwxyz"
shift=2


def main():
    enc=""
    for e in TEXT:
        if e == " ":
            enc=enc+e
        elif e in {"\n",":","!"}:
            enc=enc+e
        elif e.isupper():
            enc=enc+chr((ord(e)+shift-65)%26+65)
        else:
            enc=enc+chr((ord(e)+shift-97)%26+97)
    return print(enc)
    


##############################################################################

if __name__ == "__main__":
    main()