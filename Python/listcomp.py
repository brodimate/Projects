#!/usr/bin/env python3


def main():
    li1 = ['auto', 'villamos', 'metro']
    result1 = [e1.upper()+"!" for e1 in li1]
    li2 = ['aladar', 'bela', 'cecil']
    result2 = [e2.capitalize() for e2 in li2]
    result3 = [0 for e3 in range(10)]
    li4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result4 = [e4*2 for e4 in li4]
    li5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result5 = [int(e5) for e5 in li5]
    s6 = '1234567'
    result6 = [int(e6) for e6 in list(s6)]
    s7 = 'The quick brown fox jumps over the lazy dog'
    result7 = [len(e7) for e7 in s7.split()]
    s8 = 'python is an awesome language'
    result8 = [e8[:1] for e8 in s8.split()]
    s9 = 'The quick brown fox jumps over the lazy dog'
    result9 = [(e9, len(e9)) for e9 in s9.split()]


    print(result1)
    print()
    print(result2)
    print()
    print(result3)
    print()
    print(result4)
    print()
    print(result5)
    print()
    print(result6)
    print()
    print(result7)
    print()
    print(result8)
    print()
    print(result9)
    print()

if __name__ == "__main__":
    main()