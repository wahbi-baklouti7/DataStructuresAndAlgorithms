# Create node class
class Node:
    count_node=0
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
        # increment by 1 when create object
        Node.count_node+=1


# Create Doubly-linked list class
class DoublyLinkedList:
    # Initialize head and tail with None
    def __init__(self):
        self.head=None
        self.tail=None

    # Printing the DoublyLinkedList
    def display_list(self):
        # Check if list is empty
        if self.length()==0:
            print("List is empty")
        else:
            current_node=self.head
            string=""
            while current_node:
                string+=str(current_node.data)+" --> "
                current_node=current_node.next
            print(string.rstrip(" --> "))

    # Show the length of the list
    def length(self):
        return Node.count_node

    # Inserting at beginnign of the list
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        
        new_node.next=self.head
        self.head.previous=new_node
        self.head=new_node


    # Insertinf at end of the list
    def insert_at_end(self,data):
        # Check if list is empty
        if self.head is None:
            print("List is empty!")
        
        new_node=Node(data)
        self.tail.next=new_node
        new_node.previous=self.tail
        self.tail=new_node

    # Insert at specific postion
    def insert_by_index(self,index,data):
        if 0>index or index>self.length()-1:
            raise Exception("Index out bound")
        
        
        # if position equal 0 
        # call the method insert at beginning
        if index==0:
            self.insert_at_beginning(data)
            return
        
        # if position equal to the end of th list
        # call the method insert  at end
        if index==self.length()-1:
            self.insert_at_end(data)
            return
            
        new_node=Node(data)
        current_node=self.head
        itr=0
        while current_node:
            if itr==index-1:
                new_node.next=current_node.next
                current_node.next.previous=new_node
                current_node.next=new_node
                new_node.previous=current_node
                
            current_node=current_node.next
            itr+=1

    # Deleting at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty!")
        
        # if list contain one value
        if self.head==self.tail:
            self.tail=None
            self.head=None
            Node.count_node-=1
        
        current_node=self.head
        self.head=current_node.next
        self.head.previous=None
        current_node=None
        Node.count_node-=1


    # Deleting at end
    def deleting_at_end(self):
        if self.head is None:
            print("List is empty!")
        
        # if list contain one value
        if self.head==self.tail:
            self.tail=None
            self.head=None
            Node.count_node-=1
        
        last_node=self.tail
        self.tail=last_node.previous
        self.tail.next=None
        last_node=None
        Node.count_node-=1

    # Deleting by index
    def deleting_by_index(self,index):
        if 0>index or index>self.length():
            raise Exception("Index out bound")
        
        if self.head is None:
            print("List is empty!")
        
        # if position equal 0 
        # call the method delete at beginning
        if index==0:
            self.delete_at_beginning()
            return
        
        # if position equal to the end of th list
        # call the method delete  at end
        if index==self.length()-1:
            self.deleting_at_end()
            return

        current_node=self.head
        itr=0
        while current_node:
            if itr==index:
                current_node.previous.next=current_node.next
                current_node.next.previous=current_node.previous
                current_node=None
                Node.count_node-=1
                break
            current_node=current_node.next
            itr+=1

    # Deleting by value
    def delete_value(self,value):
        if self.head is None:
            print("List is empty!")

        current_node=self.head
        itr=0
        while current_node:
            if current_node.data==value:
                # if position equal 0 
                # call the method delete at beginning
                if itr==0:
                    self.delete_at_beginning()
                    return

                # if position equal to the end of th list
                # call the method delete  at end
                elif itr==self.length()-1:
                    self.deleting_at_end()
                    return

                current_node.previous.next=current_node.next
                current_node.next.previous=current_node.previous
                current_node=None
                Node.count_node-=1
                break
                
            current_node=current_node.next
            itr+=1

    # Reverse list
    def reverse(self):
        # Check if list is empty
        if self.length()<=1:
            return
        
        current_node=self.head
        next_node=self.head
        while next_node:
            next_node=current_node.next
            current_node.next=current_node.previous
            current_node.previous=next_node
            current_node=next_node
        
        next_node=self.head
        self.head=self.tail
        self.tail=next_node

        


test2=DoublyLinkedList()
test2.insert_at_beginning(100)
test2.insert_at_beginning(50)
test2.insert_at_beginning(444)
test2.display_list()
print("Length:",test2.length())
print("-"*40)

test2.insert_at_end(88)
test2.insert_at_end(65)
test2.display_list()
print("Length:",test2.length())
print("-"*40)

# test2.insert_by_index(4,199)
# test2.display_list()
# print("Length:",test2.length())
# print("-"*40)


# test2.insert_by_index(5,2000)
# test2.display_list()
# print("Length:",test2.length())
# print("-"*40)


test2.insert_by_index(0,1500)
test2.display_list()
print("Length is:",test2.length())
print("-"*40)


test2.delete_at_beginning()
test2.display_list()
print("Length is:",test2.length())
print("-"*40)


# test2.deleting_at_end()
# test2.display_list()
# print("Length is:",test2.length())
# print("-"*40)


test2.delete_value(444)
test2.display_list()
print("Length is:",test2.length())
print("-"*40)

test2.reverse()
test2.display_list()
print("Length is:",test2.length())
print("-"*40)




