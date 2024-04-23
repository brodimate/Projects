#!/usr/bin/env python3

def queens(li):
    li1 = [".",".",".",".",".",".","."]
    li2 = [".",".",".",".",".",".","."]
    li3 = [".",".",".",".",".",".","."]
    li4 = [".",".",".",".",".",".","."]
    li5 = [".",".",".",".",".",".","."]
    li6 = [".",".",".",".",".",".","."]
    li7 = [".",".",".",".",".",".","."]
    li8 = [".",".",".",".",".",".","."]
    li1.insert(li[0],"Q")
    li2.insert(li[1],"Q")
    li3.insert(li[2],"Q")
    li4.insert(li[3],"Q")
    li5.insert(li[4],"Q")
    li6.insert(li[5],"Q")
    li7.insert(li[6],"Q")
    li8.insert(li[7],"Q")
    
    print("+-----------------+")
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[7], m=li2[7], h=li3[7], n=li4[7], o=li5[7], ha=li6[7], he=li7[7], ny=li8[7],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[6], m=li2[6], h=li3[6], n=li4[6], o=li5[6], ha=li6[6], he=li7[6], ny=li8[6],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[5], m=li2[5], h=li3[5], n=li4[5], o=li5[5], ha=li6[5], he=li7[5], ny=li8[5],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[4], m=li2[4], h=li3[4], n=li4[4], o=li5[4], ha=li6[4], he=li7[4], ny=li8[4],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[3], m=li2[3], h=li3[3], n=li4[3], o=li5[3], ha=li6[3], he=li7[3], ny=li8[3],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[2], m=li2[2], h=li3[2], n=li4[2], o=li5[2], ha=li6[2], he=li7[2], ny=li8[2],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[1], m=li2[1], h=li3[1], n=li4[1], o=li5[1], ha=li6[1], he=li7[1], ny=li8[1],))
    print("| {e} {m} {h} {n} {o} {ha} {he} {ny} |".format(e=li1[0], m=li2[0], h=li3[0], n=li4[0], o=li5[0], ha=li6[0], he=li7[0], ny=li8[0],))
    print("+-----------------+")



def main():
    li1 = [7,3,0,2,5,1,6,4]
    li2 = [0,4,7,5,2,6,1,3]
    queens(li1)
    queens(li2)


if __name__ == "__main__":
    main()