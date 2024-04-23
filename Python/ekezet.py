#!/usr/bin/env python3
# coding: utf-8


# Kicseréli az ékezetes karaktereket ékezet nélkülire

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

t1 = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
t2 = "aeiooouuuAEIOOOUUU"

def ekezet(words):
    for i in range(0,18):
        words = words.replace(t1[i], t2[i])
    print(words)

def ekezet_dict(words):
    d = {"á": "a", "é": "e", "í": "i", "ó": "o", "ö": "o", "ő": "o", "ú": "u", "ü": "u", "ű": "u",
    "Á": "A", "É": "E", "Í": "i", "Ó": "O", "Ö": "O", "Ő": "O", "Ú": "U", "Ü": "U", "Ű": "U"}
    for k, v in d.items():
        words = words.replace(k, v)
    print(words)

def main():
    ekezet(TEXT)
    ekezet_dict(TEXT)
    
if __name__ == "__main__":
    main()