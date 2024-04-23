#!/usr/bin/env python3


def main():
    """A két szimbolum értéket összeadja aminek az értéke 2021"""
    print(sum(ord(symbol) for symbol in "ϨϽ"))


if __name__ == "__main__":
    main()