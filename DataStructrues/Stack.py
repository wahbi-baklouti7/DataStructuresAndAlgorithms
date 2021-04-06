
class Stack:
    def __init__(self):
        self.list=[]
        self.top=-1

    # Retrieve last item
    def pop(self):
        self.list.pop()
        self.top-=1
    # Added item to the list
    def push(self,item):
        self.list.append(item)
        self.top+=1

    # Check is empty
    def is_empty(self):
        if self.top==-1:
            return True
        return False