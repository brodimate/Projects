#!/usr/bin/env python3
# coding: utf-8

# Kiirja 2 ** 1000 számjegyeinek az összegét


def nsum(n):
    
    digitsum = 0
    for digit in str(n): 
      digitsum += int(digit)      
    return digitsum
   



def main():
    num = 2 ** 1000
    print(nsum(num))


if __name__ == "__main__":
    main()