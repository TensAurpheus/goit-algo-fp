class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def previous(self, cur: Node):
        prev = self.head
        if cur == self.head:
            return None
        while prev:
            if prev.next == cur:
                return prev
            prev = prev.next
            
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def sort(self):
        prev = self.head
        if (not prev) or (not prev.next):
            return self
        cur = prev.next

        while cur:
            prev = self.previous(cur)
            key = cur.data
            while prev and key < prev.data :
                    prev.next.data = prev.data
                    prev = self.previous(prev)
            if prev:
                prev.next.data = key
            else:
                self.head.data = key
            # self.print_list()
            cur = cur.next 
        return self

def merge(llist1: LinkedList, llist2: LinkedList):
        cur1 = llist1.head
        cur2 = llist2.head
        merged = LinkedList()
        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged.insert_at_end(cur2.data)
                cur2 = cur2.next
        
        while cur1:
            merged.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            merged.insert_at_end(cur2.data)
            cur2 = cur2.next
        return merged


if __name__ == '__main__':
    llist = LinkedList()
    llist2 = LinkedList()
    # List 1
    llist.insert_at_end(5)
    llist.insert_at_end(10)
    llist.insert_at_end(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print('Linked list:')
    llist.print_list()

    # Reverse List 1
    llist.reverse_list()
    print('Reversed Linked list:')
    llist.print_list()

    # Sort List 1
    llist.sort()
    print('Sorted')
    llist.print_list()

    # Filling List 2
    llist2.insert_at_end(3)
    llist2.insert_at_end(6)
    llist2.insert_at_end(9)
    llist2.insert_at_end(16)
    print('Linked list 2:')
    llist2.print_list()

    # Merge
    merged_list = merge(llist, llist2)
    print('Merged list:')
    merged_list.print_list()







