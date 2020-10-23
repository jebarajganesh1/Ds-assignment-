class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
    def display(self):
        print(self.element)

class LinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
        

        
    def __len__(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        print(first.element)
        first = first.next
        while first:
            
            print(first.element)
            first = first.next
    
    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            self.size -= 1
            
    def add_between_list(self,position,element):
        if position > self.size:
            print("Index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position-1)
            current_node = self.get_node_at(position)
            prev_node.next = element
            element.next = current_node
            self.size -= 1
        
    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size
          
