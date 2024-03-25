'''
The aim is to design a queue abstract data type with the help of stacks.
'''

class Queue:
    def __init__(self):
        self.stack_enqueue = []

    def enqueue(self, data):
        self.stack_enqueue.append(data)

    def dequeue(self):
        if len(self.stack_enqueue) == 1:
            return self.stack_enqueue.pop()

        temp = self.stack_enqueue.pop()
        target = self.dequeue()
        self.stack_enqueue.append(temp)
        return target

    def size(self):
        return len(self.stack_enqueue)


q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
