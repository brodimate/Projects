#!/usr/bin/env python3

data = [ 
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)
]

lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

li=[ [2,6],[1,3],[5,4] ]

def my_func1(t):
    return t[3]

def my_func2(user):
    return int(user.split(":")[0])

def my_func3(li):
    return li[1]


def main():
    result = sorted(data, key=my_func1)
    print(result)
    print("-" * 20)
    result2 = sorted(lst, key=my_func2, reverse=True)
    print(result2)
    print("-" * 20)
    result3 = sorted(li, key=my_func3)
    print(result3)

if __name__ == "__main__":
    main()