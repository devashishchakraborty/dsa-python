class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node 

        else:
            new_node = Node(data)
            cur = self.head 
            while cur.next:
                cur = cur.next 
            cur.next = new_node 
            new_node.prev = cur 

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next 
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur 
                nxt.prev = new_node
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next
    
    def delete(self, key):
        curr = self.head
        while curr:

            if curr.data == key and curr == self.head:
                # Case 1: Deleting the Only Node
                if not curr.next:
                    curr = None
                    self.head = None
                    return
            
                # Case 2: Deleting the Head Node
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
            
            elif curr.data == key:
                # Case 3
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    
                    prev.next = nxt
                    nxt.prev = prev
                    

                    curr.next = None
                    curr.prev = None
                    curr = None

                    return
                # Case 4
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return

            curr = curr.next
    
    def delete_node(self, node):
        curr = self.head
        while curr:

            if curr == node and curr == self.head:
                # Case 1: Deleting the Only Node
                if not curr.next:
                    curr = None
                    self.head = None
                    return
            
                # Case 2: Deleting the Head Node
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
            
            elif curr == node:
                # Case 3
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                # Case 4
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next
    
    def remove_duplicates(self):
        curr = self.head
        dup_values = dict()
        prev = None

        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                self.delete_node(curr)
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next

    def print_list(self):
        curr = self.head 
        while curr:
            print(curr.data)
            curr = curr.next
    
    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp

            curr = curr.prev
        
        if temp:
            self.head = temp.prev
            




dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()