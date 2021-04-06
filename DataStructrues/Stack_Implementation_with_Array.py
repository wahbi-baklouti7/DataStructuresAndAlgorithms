# Create Stack class
class Stack:
    def __init__(self,size):
        self.size=size
        self.list=[]
        self.top=-1

    # get the length of the Stack
    def __len__(self):
        return len(self.list)
    
    # Check if the Stack is empty
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    # Retrive the last item 
    def pop(self):
        #check if stack is empty or not
        if self.is_empty():
            raise Exception("Underflow, Stack is empty")
        else:
            self.top-=1
            return self.list.pop()
            
    
    # Added item to the Stack
    def push(self,item):
        # Check if Stack is full
        if self.top==self.size-1:
            raise Exception("Overflow, Stack is full")
        else:
            self.list.append(item)
            self.top+=1
    # Show the Peek of Stack
    def peek(self):
        # Check if Stack is empty
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Peek is:",self.list[self.top])
    
    # Printing the list
    def display(self):
        # Check if Stack is empty
        if self.is_empty():
            print("Stack is empty!")

        for n in range(self.top,-1,-1):
            print(""+str(self.list[n]))
            
            


st=Stack(5)
st.push(10)
st.push(55)
st.push(105)
st.push(35)
st.push(86)
st.display()
print("length is:",len(st))
print("-"*20)

st.pop()
st.display()
print("length is:",len(st))
print("-"*20)
st.peek()
print("-"*20)
print("length is:",len(st))
st.display()

print("length is:",len(st))

