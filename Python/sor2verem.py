#!/usr/bin/env python3


class MyQueue():

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if len(self.stack_2) == 0:
            if len(self.stack_1) == 0:
                raise IndexError("Can't dequeue from empty queue!")
            while len(self.stack_1) > 0:
                last_stack_1_item = self.stack_1.pop()
                self.stack_2.append(last_stack_1_item)
        return self.stack_2.pop()


    def __str__ (self):
            return "{s1}".format(s1=str(self.stack_1))
def main():
    q = MyQueue()
 
    for i in range(5):
        q.enqueue(i)
     
    for i in range(5):
        print(q.dequeue())
        
if __name__ == '__main__':
    main()