class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1


    def enqueue(self,value):

        # Check if the queue is full
        if self.is_full():
            raise Exception("Queue is full!")
        # if the queue is empty
        if self.is_empty():
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=value
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=value



    def dequeue(self):
        # Check if queue is empty
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            data=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return data

    def is_empty(self):
        if self.rear==-1:
            return True
        return False

    def is_full(self):
        if (self.rear+1)%self.size==self.front:
            return True
        return False

    # Display the queue 
    def display(self):
        string=""
        ptr=self.front
        while ptr!=self.rear:
            string+=str(self.queue[ptr])+","
            ptr=(ptr+1)%self.size
        string+=str(self.queue[ptr])
        return string


cq=CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(5)
cq.enqueue(8)
cq.enqueue(100)
print("-"*30)


print(cq.display())
print("-"*30)

print("Delete:",cq.dequeue())
print(cq.display())
print("-"*30)

cq.enqueue(404)
print(cq.display())
print("-"*30)

print("Delete:",cq.dequeue())
print(cq.display())
print("-"*30)

cq.enqueue(5555)
print(cq.display())
