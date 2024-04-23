#!/usr/bin/env python3


def main():
    li = []
    f = open("day02.txt", "r")
    for line in f:
        li.append([int(i) for i in line.split()])

    checksum = sum(max(line) - min(line) for line in li)
    print(checksum)

    f.close()

if __name__ == "__main__":
    main()