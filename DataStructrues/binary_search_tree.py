# from Queue_using_Array import Queue

#create node class
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

# Create Binary Tree class
class Binary_tree:
    def __init__(self):
        self.root=None


    # Display the binary tree
    def dispaly(self):
        if self.root is None:
            print("Tree is empty")
        else:
            return self._display(self.root,"")
    
    def _display(self,current_node,string):
        if current_node:
            
            string=self._display(current_node.left,string)
            string+=str(current_node.data)+"-"
            string=self._display(current_node.right,string)
        return string


    # insert value into the binary tree
    def add_value(self,value):
        # if the tree is empty
        # the first value added
        # will be the root of tree
        if self.root is None:
            self.root=Node(value)
        
        else:
            self._add_value(value,self.root)
    
    def _add_value(self,value,current_node):
            """current_node ==> root"""
            # if value is bigger than 
            # the root value
            # so we add at the left sub-tree
            if value>current_node.data:
                # if the right child does not exist
                # we will insert the value at the right side
                if current_node.right is None:
                    current_node.right=Node(value)
                else:
                    self._add_value(value,current_node.right)
            
            elif value<current_node.data:
                # if the left child does not exist
                # we will insert the value at the right side
                if current_node.left is None:
                    current_node.left=Node(value)
                else:
                    self._add_value(value,current_node.left)


    # Search for value in Binary Search Tree
    def search(self,value):
        if self.root:
            is_find=self._search(value,self.root)
            if is_find:
                return True
            return False
        return "Tree is empty"

    def _search(self,value,current_node):
        if current_node:
            if value==current_node.data:
                return True
            elif value>current_node.data :
                return self._search(value,current_node.right)
            elif value<current_node.data :
                return self._search(value,current_node.left)
            
        return False


    # Find the max value in the Binary Search Tree
    def get_max(self):
        # Check if the Tree is empty
        if self.root is None:
            print("Tree is empty")
        
        # if the Tree contain one element
        elif not self.root.left  and not self.root.right:
            return self.root.data
        else:
          return self._get_max(self.root.right) 
    
    def _get_max(self,current_node):
        
        while current_node.right:
            current_node=current_node.right
        return current_node.data


    # Find the min value in the Binary Search Tree
    def get_min(self):
        # Check if the Tree is empty 
        if self.root is None:
            print("Tree is empty")
        
        # if the Tree contain one element
        elif not self.root.left  and not self.root.right:
            return self.root.data
        
        else:
            return self._get_min(self.root.left)
    
    def _get_min(self,current_node):
        if current_node.left:
            return self._get_min(current_node.left)
        return current_node.data


    # Deleting value from the Tree
    def delete(self,value):
        if self.root is None:
            raise Exception("Tree is empty")
        else:
            return self._delete(value,self.root)

    def _delete(self,value,current_node):
        if current_node:
            if value>current_node.data:
               current_node.right= self._delete(value,current_node.right)
            elif value<current_node.data:
               current_node.left= self._delete(value,current_node.left)

            else:
                # if is a leaf
                if not current_node.left and not current_node.right:
                    current_node=None
                    
                # if has one child
                elif not current_node.left:
                    current_node=current_node.right
                elif not current_node.right:
                    current_node=current_node.left

                # if has two child
                else:
                    tem=self._get_max(current_node.left)
                    current_node.data=tem
                    current_node.left=self._delete(tem,current_node.left)
            return current_node
        raise Exception("Invalid value")


    # Level traversal order
    def level_traversal_order(self):
        if not self.root:
            raise Exception("Tree is empty")
        if not self.root.left and not self.root.right:
            return self.root.data

        else:
            return self._level_traversal_order(self.root)

    def _level_traversal_order(self,current_node):
        string=""
        queue=Queue(20)
        queue.enqueue(current_node)
        while not queue.is_empty():
            
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            
            value=queue.dequeue()
            string+=str(value.data)+"-"
            current_node=queue.peek()
        return string[:-1]








binartytree=Binary_tree()
binartytree.add_value(10)
binartytree.add_value(17)
binartytree.add_value(12)
binartytree.add_value(7)
binartytree.add_value(18)
binartytree.add_value(8)
binartytree.add_value(11)
binartytree.add_value(9)
binartytree.add_value(66)
binartytree.add_value(6)
binartytree.add_value(5)


print("Max value is:",binartytree.get_max())
print("-"*30)
print(binartytree.dispaly())
print("-"*30)
print("Min value is:",binartytree.get_min())
binartytree.delete(10)
print("-"*30)
print(binartytree.dispaly())
print("-"*30)
print("Min value is:",binartytree.get_min())
print("-"*30)
print("Max value is:",binartytree.get_max())
print("-"*30)
# print(binartytree.level_traversal_order())
