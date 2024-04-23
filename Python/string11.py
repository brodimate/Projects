#!/usr/bin/env python3
# coding: utf-8


def donuts(count):
    if count < 10:
        return "Fánkok száma: {c}".format(c=count)
    else:
        return "Fánkok száma: sok"  


def both_ends(s):
    if len(s) > 2:
        return s[:2] + s[-2:]
    else:
        return ""  



def fix_start(s):
    elso = s[:1]
    masodik = s[1:].replace(elso, "*")
    return "{e}{m}".format(e = elso, m = masodik)



def mix_up(a, b):
    elso = a.replace(a[:2], b[:2])
    masodik = b.replace(b[:2], a[:2])
    return "{e} {m}".format(e = elso, m = masodik)




def main():
    print('donuts')
    print()
    print('both_ends')
    print()
    print('fix_start')
    print()
    print('mix_up')
  

#############################################################################

if __name__ == '__main__':
    main()
