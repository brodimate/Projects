#!/usr/bin/env python3   

# Kiirja a listáját azoknak a celláknak amik nyitva maradtak.
    
    
def main(): 
    n_doors = 600
    doors = [0] * n_doors
    for i in range(1, n_doors+1):
        doors[i-1::i] = [(x+1)%2 for x in doors[i-1::i]]

    open_doors = []
    for index, element in enumerate(doors):
        if element:
            open_doors.append(index+1)

    # print(''.join([str(e) for e in open_doors]))
    print(open_doors)

if __name__ == "__main__":
    main()