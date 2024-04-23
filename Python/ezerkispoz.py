#!/usr/bin/env python3


# Az 1000 alatti számokból összeadja ami oszható 3al és 5el.

def main():
    result = [e for e in range(1,1000) if e%3==0 or e%5==0] 
    """Egy 0-999ig terjedő listából csak a 3al es az 5el osztható számokat szedi ki.
    
    Összeadja ezeket a számokat"""
    print (sum(result))
    


if __name__ == "__main__":
    main()