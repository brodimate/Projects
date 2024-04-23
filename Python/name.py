#!/usr/bin/env python3


# A szkript bekér egy stringet, amibőlmlevágja a whitespace karaktereket a végéről és az elejéről , ami után köszönti azt a személyt.


def main():
    s = input("Név: ")
    print("Hello " + s.strip() + "!")


if __name__ == "__main__":
    main()
