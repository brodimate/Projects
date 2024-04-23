#!/usr/bin/env python3
# coding: utf-8

# Visszaadja egy lista mediánját
def the_median(li):
    n = len(li)
    s = sorted(li)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2]


def main():
    li1 = [2, 3, 4, 5, 6]
    li2 = [2, 3, 4, 5]
    print(the_median(li1))
    print(the_median(li2))


if __name__ == "__main__":
    main()