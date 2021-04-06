from  stack1 import Stack


class Queue_Stack:
    def __init__(self):
        self.stack11=Stack()
        self.stack2=Stack()

    def enqueue(self,data):
        self.stack11.push(data)
    

    def dequeue(self):
        top=self.stack11.top
        for n in range(self.stack11.top+1):
            self.stack2.push(self.stack11.pop())
        
        self.stack2.pop()
        for j in range(self.stack2.top+1):
            self.stack11.push(self.stack2.pop())


    def printing(self):
        self.stack11.display()


qs=Queue_Stack()
qs.enqueue(10)
qs.printing()
print("-"*30)

qs.enqueue(50)
qs.printing()
print("-"*30)

qs.enqueue(666)
qs.printing()
print("-"*30)

qs.enqueue(888)
qs.printing()
print("-"*30)

qs.dequeue()
qs.printing()
print("-"*30)