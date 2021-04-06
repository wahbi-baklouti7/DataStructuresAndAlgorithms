# Create node class
class Node:
    count_node=0
    def __init__(self,data):
        self.data=data
        self.next=None
        # increment by 1 when create object
        Node.count_node+=1

# Create Circler Linked-List
class CirclerLinkedList:
    # Initialize tail with None
    def __init__(self):
        self.tail=None

    # Display the list
    def display_list(self):
        # Check if list is empty
        if self.length()==0:
            print("List is empty")
        else:
            current_node=self.tail.next
            string=""
            while current_node.next!=self.tail.next:
                string+=str(current_node.data)+" --> "
                current_node=current_node.next
            string=string+str(current_node.data)
            print(string)
    
    # Show the length of list
    def length(self):
        return Node.count_node
            
    # Insert at beginning
    def Insert_at_beginning(self,data):
        new_node=Node(data)
        
        if self.tail is None:
            self.tail=new_node
            self.tail.next=new_node
            return
        new_node.next=self.tail.next
        self.tail.next=new_node
    
    # Inserting at end
    def insert_at_end(self,data):
        if self.tail is None:
            print("List is empty")
        
        new_node=Node(data)
        
        new_node.next=self.tail.next
        self.tail.next=new_node
        self.tail=new_node
        
    # Inserting at specific position
    def insert_at_position(self,position,data):
        if 0>position or position>self.length():
            raise Exception ("Index out bound!")
        
        
        # if position equal 0 
        # call the method insert at beginning
        if position==0:
            self.Insert_at_beginning(data)
            return
        
        # if position equal to last index
        # call method insert at end
        if position==self.length()-1:
            self.insert_at_end(data)
            return
        new_node=Node(data)
        current_node=self.tail.next
        itr=0
        while current_node.next!=self.tail.next:
            if itr==position-1:
                new_node.next=current_node.next
                current_node.next=new_node
            current_node=current_node.next
            itr+=1
        
    # Deleting at beginning
    def deleting_at_beginning(self):
        if self.tail is None:
            print("List is empty")
        
        # if list contain one value
        if self.tail.next==self.tail:
            self.tail=None
            Node.count_node-=1
            return
        
        first_node=self.tail.next
        self.tail.next=first_node.next
        first_node=None
        Node.count_node-=1


    # Deleting at end
    def deleting_at_ending(self):
        if self.tail is None:
            print("List is empty")
        
        # if list contain one value
        if self.tail.next==self.tail:
            self.tail=None
            Node.count_node-=1
            return
        
        current_node=self.tail.next
        previous_node=current_node
        while current_node.next!=self.tail.next:
            previous_node=current_node
            current_node=current_node.next
        
        previous_node.next=self.tail.next
        self.tail=previous_node
        current_node=None
        previous_node=None
        Node.count_node-=1


    # Deleting at specific position
    def delete_by_index(self,index):
        if 0> index or index>self.length()-1:
            raise Exception ("Index out bound!")
        
        # If position is 0 call method 
        # delete at beginning
        if index==0:
            self.deleting_at_beginning()
            return
        
        # If position equal to length of list
        # call method delete at end
        if index==self.length()-1:
            self.deleting_at_ending()
            return


        current_node=self.tail.next
        itr=0
        while current_node.next!=self.tail.next:
            if itr==index-1:
                current_node.next=current_node.next.next
                Node.count_node-=1
            current_node=current_node.next
            itr+=1
        

    # Deleting by value
    def delete_by_value(self,value):
        if self.tail is None:
            print("List is empty!")

        current_node=self.tail.next
        previous_node=current_node 
        itr=0
        while itr < self.length():
            if current_node.data==value:
                # if index is 0 call 
                # mehtod deleteing at beginning
                if itr==0:
                    self.deleting_at_beginning()
                    return
                
                # if index equal to length-1
                # call method deleting at ending
                if itr==self.length()-1:
                    self.deleting_at_ending()
                    return
                
                previous_node.next=current_node.next
                current_node=None
                Node.count_node-=1
                break
            previous_node=current_node
            current_node=current_node.next
            itr+=1
        else:
            raise Exception("Invalid value")

           

    #reverse Circlar list
    def reverse(self):
        if self.length()<=1:
            return
        next_node=self.tail.next
        previous_node=None
        current_node=self.tail.next
        while next_node.next!=self.tail.next:
            next_node=current_node.next
            current_node.next=previous_node
            previous_node=current_node
            current_node=next_node
        
        self.tail=self.tail.next
        current_node.next=previous_node
        self.tail.next=current_node
        
        




test3=CirclerLinkedList()
test3.Insert_at_beginning(10)
# test3.Insert_at_beginning(90)
# test3.Insert_at_beginning(45)
test3.display_list()
print("length:",test3.length())
print("-"*40)

test3.insert_at_end(44)
test3.insert_at_end(15)
test3.insert_at_end(999)
test3.display_list()
print("length:",test3.length())
print("-"*40)

test3.insert_at_position(3,50)
test3.display_list()
print("length:",test3.length())
print("-"*40)

# test3.deleting_at_beginning()
# test3.display_list()
# print("length:",test3.length())
# print("-"*40)

# test3.deleting_at_beginning()
# test3.display_list()
# print("length:",test3.length())
# print("-"*40)

# test3.deleting_at_ending()
# test3.display_list()
# print("length:",test3.length())
# print("-"*40)

# test3.delete_by_index(0)
# test3.display_list()
# print("length:",test3.length())
# print("-"*40)

# test3.delete_by_value(15)
# test3.display_list()
# print("length:",test3.length())
# print("-"*40)

test3.reverse()
test3.display_list()
print("length:",test3.length())
print("-"*40)




