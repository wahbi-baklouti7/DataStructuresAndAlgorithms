
# Create Queue class
class Queue:
    def __init__(self,size):
        self.size=size
        self.buffer=[0]*self.size
        self.front=-1
        self.rear=-1


    # Display the length of the Queue
    def __len__(self):
        return len(self.buffer)
    
    # Add item onto the Queue
    def enqueue(self,value):
        if self.is_full():
            raise Exception("Overflow, Queue is full")
        
        elif self.is_empty():
            self.front+=1
            self.rear+=1
            self.buffer[self.rear]=value
        
        else:
            self.rear+=1
            self.buffer[self.rear]=value
            
            
    # Remove item from the Queue
    def dequeue(self):
        # Check if Queue is empty
        if self.is_empty():
            raise Exception("Underflow, Queue is empty")
        else:
            temp=self.buffer[self.front]
            self.front+=1
            return temp
    
    # Show the peek in the Queue
    def peek(self):
        if self.is_empty():
            # raise Exception("Underflow, Queue is empty")
            return
        
        else:
            return self.buffer[self.front]
    
    
    # Check if the Queue is empty
    def is_empty(self):
        if self.front==-1:
            return True
        if self.front>self.rear:
            return True
        return False

    # Check if Queue is full
    def is_full(self):
        if self.rear>=self.size-1:
            return True
        
        return False

    # Display the Queue
    def display(self):
        i=self.front
        string=""
        while i<=self.rear:
            string+=str(self.buffer[i])+","
            i+=1
        string=string[:-1]
        print(string)

qu=Queue(6)

qu.enqueue(10)
qu.enqueue(80)
qu.enqueue(5)
qu.enqueue(55)
qu.enqueue(4)
qu.display()
print("-"*30)
qu.enqueue(99)
qu.display()
print("length:",len(qu))
print("-"*30)
qu.dequeue()
qu.display()
print("-"*30)
qu.dequeue()
qu.dequeue()
qu.display()
print("-"*30)




