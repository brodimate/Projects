#!/usr/bin/env python3

import re

def main():

    pattern = 'jsun'
    words = []

    pattern = re.compile(".*j.*s.*u.*n.*")

    with open("corpus.csv", 'r') as f:
        for line in f:
            word = line.strip().split(',')[0].lower()
            if pattern.match(word):
                words.append(word)

    for word in words:
        print(word)

if __name__ == "__main__":
    main()