#!/usr/bin/env python3

# Kiirja az osszes Münchausen-számot

def main():
    for i in range(0,440000000):
        nums = (int(num) for num in str(i))
        """Végig megy az összes számon a range-ben
        
        Ha a számok karaktereinek osszege megegyezik az eredeti számmal akkor kiírja"""
        if sum(num ** num for num in nums) == i or i == 0:
            """Mivel tul sok a szám így ez nagyon lassú"""
            print(i) 
    
    


if __name__ == "__main__":
    main()