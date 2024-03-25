'''
The aim is to design a queue abstract data type with the help of stacks.
'''

class Queue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, data):
        self.stack_enqueue.append(data)

    def dequeue(self):
        if len(self.stack_dequeue) == 0:
            len_org = len(self.stack_enqueue)
            for i in range(len_org):
                self.stack_dequeue.append(self.stack_enqueue.pop())

        if len(self.stack_dequeue) != 0:
            return self.stack_dequeue.pop()
        else:
            return None

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)


q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
