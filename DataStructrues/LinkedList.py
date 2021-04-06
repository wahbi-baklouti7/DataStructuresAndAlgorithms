class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#create LinkedList class to add functionality 
class LinkedList:
    def __init__(self):
        self.head=None

    #show the list
    
    def display_list(self):
        current_node=self.head
        value=""
        while current_node:
            value+=str(current_node.data)+" --> "
            current_node=current_node.next
        print(value.rstrip(" --> "))
        
    #count the number of node
    def get_length(self):
        count=0
        if self.head is None:
            print("list is empty!")
        current_node=self.head
        while current_node:
            count+=1
            current_node=current_node.next
        return count
       

    #insertion at end
    def insertion_at_end(self,data):
        #create a node
        new_node=Node(data)

        #check if this is the first node
        #if no will be the the head if no we will append the new node
        #at end and the pointer will point to new node
        if self.head is None:
            self.head=new_node
            return

        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
    
    #insert data at the beginning of list
    def insertion_at_beginning(self,data):
        #create a node
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    #inserting by specific position
    def insert_at_position(self,position,data):
        if self.head is None:
            print("list is empty!")
        
        if 0<position or position>self.get_length():
            raise Exception ("Invalid index")

        if position==0:
            self.insertion_at_beginning(data)
            return
        
        new_node=Node(data)
        current_node=self.head
        i=0
        while i!=position-1:
            current_node=current_node.next
            i+=1
        new_node.next=current_node.next
        current_node.next=new_node

    #delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("list is empty!")
        if self.get_length()==1:
            self.head=None

        current_node=self.head
        self.head=current_node.next
        current_node=None
        # new_head=self.head
        # new_head=self.head.next
        # self.head=new_head

    #delete at end
    def delete_at_end(self):
        if self.head is None:
            print("list is empty!")
        current_node=self.head
        prev_node=self.head
        while current_node.next:
            prev_node=current_node
            current_node=current_node.next
        prev_node.next=0
        current_node=None
    
    
    #delete at specific position
    def delete_by_index(self,index):
        if 0>index or index>=self.get_length():
            raise Exception ("invalid index")
        if self.head is None:
            print("list is empty!")
        if index==0:
            self.delete_at_beginning()
        
        itr=0
        current_node=self.head
        prev_node=self.head
        while current_node:
            prev_node=current_node
            if itr==index-1:
                prev_node.next=current_node.next.next
                current_node=None

                break
            current_node=current_node.next
            itr+=1

    #delete by value
    def delete_by_value(self,value):
        if self.head is None:
            print("list is empty!")
        
        current_node=self.head
        if self.head.data==value:
            self.head=current_node.next
            return
        
        prev_node=self.head
        while current_node:
            if current_node.data==value:
                prev_node.next=current_node.next
                current_node=None
                break
            prev_node=current_node
            current_node=current_node.next
        raise Exception ("value not in the list")        





test1=LinkedList()
test1.insertion_at_end(10)
test1.insertion_at_end(50)
test1.insertion_at_end(47)
test1.insertion_at_beginning(1000)
test1.insertion_at_beginning(555)
test1.insert_at_position(0,999)
test1.display_list()
test1.delete_at_beginning()
test1.display_list()
test1.delete_at_beginning()
test1.display_list()
test1.delete_at_end()
test1.insertion_at_end(666)
test1.display_list()
print(test1.get_length())
print("-"*40)
# test1.delete_by_index(4)
test1.display_list()
print(test1.get_length())
print("-"*40)
test1.insertion_at_end(222)
test1.display_list()
print(test1.get_length())
print("-"*40)
test1.insertion_at_end(444)
test1.display_list()
print(test1.get_length())
print("-"*40)
test1.delete_by_value(15000)
test1.display_list()
print(test1.get_length())
print("-"*40)
# test1.delete_by_index(4)
# test1.display_list()
# print(test1.get_length())
# print("-"*40)





