# Create node class
class Node:
    count=0
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
        # increment by 1 when create object
        Node.count+=1


# Create CircularDoublyLinkedList
class CircularDoublyLL:
    # Initialize head and tail with None
    def __init__(self):
        self.head=None
        self.tail=None
    
    # show the length of the list
    def length(self):
        return Node.count

    # Printing the all values of the list
    def display(self):
        #check if list is empty
        if self.length()==0:
            print("List is empty")
        else:
            current_node=self.head
            string=""
            while current_node!=self.tail:
                string+=str(current_node.data)+" --> "
                current_node=current_node.next
            string+=str(current_node.data)
            print(string)

    # Insert value at beginning
    def preappend(self,data):
        new_node=Node(data)
        
        #Check if list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.head.previous=new_node
            self.tail.next=new_node
            return
        
        new_node.next=self.head
        self.head.previous=new_node
        new_node.previous=self.tail
        self.tail.next=new_node
        self.head=new_node

    # Insert value at ending
    def append(self,data):
        new_node=Node(data)
        
        #Check if list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.head.previous=new_node
            self.tail.next=new_node
            return
        
        self.tail.next=new_node
        new_node.previous=self.tail
        new_node.next=self.head
        self.head.previous=new_node
        self.tail=new_node

    # Inserting value at specific position
    def insert_by_index(self,index,data):
        # Check if index is valide
        if 0>index or index>=self.length():
            raise Exception("Index out bound")
        
        # Check if list is empty
        if self.head is None:
            print("List is empty!")
        
        # if index is 0 call method preappend
        if index==0:
            self.preappend(data)
            return
        
        # if index equal to last index 
        # call methon append
        if index==self.length()-1:
            self.append(data)
            return

        new_node=Node(data)
        current_node=self.head
        itr=0
        while current_node != self.tail:
            if itr==index-1:
                new_node.next=current_node.next
                current_node.next.previous=new_node
                current_node.next=new_node
                new_node.previous=current_node
                break
            current_node=current_node.next
            itr+=1

    # Deleting value form beginning
    def deleting_at_beginning(self):
        # Check if list is empty
        if self.head is None:
            print("List is empty!")
        
        # if list contain one value
        if self.head==self.tail:
            self.head=None
            self.tail=None
            Node.count-=1
            return

        
        current_node=self.head
        self.head=current_node.next
        self.head.previous=self.tail
        self.tail.next=self.head
        current_node=None
        Node.count-=1
    
    # Deleting value from ending
    def deleting_at_ending(self):
        # Check if list is empty
        if self.head is None:
            print("List is empty!")
        
        # if list contain one value
        if self.head==self.tail:
            self.head=None
            self.tail=None
            Node.count-=1
        
            return
        current_node=self.tail
        self.tail=current_node.previous
        self.tail.next=self.head
        current_node=None
        Node.count-=1
    
    # Delete value form the list by index
    def deleting_by_index(self,index):
        # Check if index is valide
        if 0>index or index>=self.length():
            raise Exception("Index out bound")
        
        # Check if list is empty
        if self.head is None:
            print("List is empty!")

        # if index is 0 call 
        # method deleteing at beginning
        if index==0:
            self.deleting_at_beginning()
            return
        
        # if index equal to length-1
        if index==self.length()-1:
            self.deleting_at_ending()
            return

        current_node=self.head
        itr=0
        while current_node != self.tail:
            
            if itr==index:
                current_node.previous.next=current_node.next
                current_node.next.previous=current_node.previous
                current_node=None
                Node.count-=1
                break
            current_node=current_node.next
            itr+=1
    
    # Deleting from list by value
    def delete_by_value(self,value):
        # Check if list is empty
        if self.head is None:
            print("List is empty!")

        current_node=self.head
        itr=0
        flag=0
        while itr < self.length():
            if current_node.data==value:
                # if index is 0 call 
                # method deleteing at beginning
                if itr==0:
                    self.deleting_at_beginning()
                    return
                
                # if index equal to length-1
                # call method deleting at ending
                if itr==self.length()-1:
                    self.deleting_at_ending()
                    return
                
                current_node.previous.next=current_node.next
                current_node.next.previous=current_node.previous
                current_node=None
                Node.count-=1
                flag=1
                break
            current_node=current_node.next
            itr+=1
        # Check if value exist or not
        if flag==0:
            raise Exception("Value does not exist!")
    
    # Reverse the list
    def reverse(self):
        if self.length()<=1:
            return
        
        current_node=self.head
        next_node=self.head
        while next_node != self.tail:
            next_node=current_node.next
            current_node.next=current_node.previous
            current_node.previous=next_node
            current_node=next_node
        
        current_node.next=current_node.previous
        current_node=self.tail
        # Change the value of the head and  the tail
        self.tail=self.head
        self.head=current_node
        self.head.previous=self.tail
        self.tail.next=self.head

            
            




    



test4=CircularDoublyLL()
test4.preappend(10)
test4.display()
print("Length:",test4.length())
print("-"*30)
test4.preappend(50)
test4.display()
print("Length:",test4.length())
print("-"*30)
test4.append(100)
test4.display()
print("Length:",test4.length())
print("-"*30)

test4.append(666)
test4.display()
print("Length:",test4.length())
print("-"*30)

test4.insert_by_index(3,200)
test4.display()
print("Length:",test4.length())
print("-"*30)

# test4.deleting_at_beginning()
# test4.display()
# print("Length:",test4.length())
# print("-"*30)

# test4.deleting_at_ending()
# test4.display()
# print("Length:",test4.length())
# print("-"*30)

# test4.deleting_by_index(0)
# test4.display()
# print("Length:",test4.length())
# print("-"*30)

# test4.delete_by_value(100)
# test4.display()
# print("Length:",test4.length())
# print("-"*30)

test4.reverse()
test4.display()
print("Length:",test4.length())
print("-"*30)
