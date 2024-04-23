#!/usr/bin/env python3


def product(nums):
    p = 1
    for e in nums:
        p *= e
    return p


def main():
    li = [1, 2, 3, 4, 5]
    result = product(li)
    print(result)

if __name__ == "__main__":
    main()