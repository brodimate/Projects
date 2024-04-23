#!/usr/bin/env python3


# Megnézi, hogy helyesek-e a zárójelek

nyito = ["[","{","("]
zaro = ["]","}",")"]
  
def zarojelek(s):
    li = []
    for e in s:
        if e in nyito:
            li.append(e)
        elif e in zaro:
            p = zaro.index(e)
            if ((len(li) > 0) and (nyito[p] == li[len(li)-1])):
                li.pop()
            else:
                return False
    if len(li) == 0:
        return True
    else:
        return False
  

def main():
    print(zarojelek("()[]{}"))


if __name__ == "__main__":
    main()