#!/usr/bin/env python3

# kitörli a string1.py-bol a #-el kezdődő sorokat


def main():
    f = open("string1.py", "r")
    to = open("string1_clean.py", "w")

    for line in f:
        if line.startswith("#") or line.startswith("    #"):
            continue
        else:
            to.write(line)

    f.close()
    to.close()


if __name__ == "__main__":
    main()