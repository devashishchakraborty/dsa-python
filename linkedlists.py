class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, previous_node, data):
        if not previous_node:
            print("Previous Node doesn't exist.")
            return 
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node
    
    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None
    
    def delete_node_at_position(self, position):
        if self.head:
            current_node = self.head
            if position == 0:
                self.head = current_node.next
                current_node = None
                return
        
            prev = None
            count = 0

            while current_node and count != position:
                prev = current_node
                current_node = current_node.next
                count += 1
        
            if current_node is None:
                return
        
            prev.next = current_node.next
            current_node = None
        
    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)
    
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p
        
        self.head = new_head
        return self.head
    
    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()

        while curr:
            if curr.data in dup_values:
                # Remove Node
                prev.next = curr.next
                curr = None
            else:
                # Have Not Encountered this Value before
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next
        
    def print_nth_from_last(self, n, method):
        if method == 1:
            total_len = self.len_iterative()

            curr = self.head
            while curr:
                if total_len == n:
                    #print(curr.data)
                    return curr.data
                total_len -= 1
                curr = curr.next
            if curr is None:
                return

        if method == 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n:
                        break
                    q = q.next
                
                if not q:
                    print(str(n) + " is greater than the number of nodes in list")
                    return 
                
                while p and q.next:
                    p = p.next
                    q = q.next

                return p.data

            else:
                return None
    
    def count_occurences_iterative(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count
    
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
    
    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev

            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None
    
    def is_palindrome_1(self):
        # Solution 1
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]
    
    def is_palindrome_2(self):
        # Solution 2
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1

            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self,method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()
    
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        if self.head and llist.head:
            while p and q:
                q.data = int(q.data) + int(p.data) + carry
                if q.data >= 10:
                    carry = 1
                p = p.next
                q = q.next
            return q
                
        
    

# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist = LinkedList()

llist.append(4)
llist.append(5)
llist.append(8)

llist2 = LinkedList()
llist.append(4)
llist.append(5)
llist.append(8)

llist.sum_two_lists(llist2)
llist.print_list()