"""
This module provides basic functions and implementations for testing Linked Lists in python
"""
from datetime import datetime
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def remove_node(head, val):
    dummy = Node(next=head)
    iter = dummy
    try:
        while iter.next and iter.next.val != val: 
            iter = iter.next
        if iter.next and iter.next.val == val: #removed head
            iter.next = iter.next.next
            return dummy.next
        else:
            print(f"{val} does not exist in linked list")
            return head
    except Exception as e:
        print(f"An error occurred: {e}")
        return head
    
def insert_end(head, val): #More like append node
    dummy = Node(val)
    iter = head
    try:
        while iter.next != None:
            iter = iter.next
        #When iter.next == None, meaning we are at the end of the Linked List, insert
        iter.next = dummy
        return head
    except Exception as e:
        print(f"Error has occured, node could not be added {e}")
        return head

def insert_beginning(head,val):
    dummy = Node(val,head)
    head = dummy
    return head


def search(head,val):
    iter = head
    try:
        while iter is not None:
            if iter.val == val:
                return iter
            iter = iter.next
        return None
    except Exception as e:
        print(f"Error has occured: {e}")
        return head

def reverse_linked_list(head):
    prev = None
    current = head
    try:
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head
    except Exception as e:
        print(f"An error has occured {e}")
        return None

def print_linked_list(head):
    if head is None:
        print("Empty list")
        return
    s = ""
    while head is not None:
        s += str(head.val) + " -> "
        head = head.next
    s += "None"
    print(s)

def main():
    # arr = list(range(100000000))

    # #Remove num time from array
    # print("Array Removal")
    # start_time = datetime.now()
    # arr.remove(853)
    # end_time = datetime.now()
    # print(f"Execution time:{end_time - start_time}")


    # #Populate our Linked List the same way

    # head = Node(0,None)
    # iter = head
    # for i in range(1,100000000):
    #     iter.next = Node(i,None)
    #     iter = iter.next

    # #Now remove same 853 from LinkedList

    # print("Linked List Removal")
    # start_time = datetime.now()
    # remove_node(head,853)
    # end_time = datetime.now()
    # print(f"Execution time:{end_time - start_time}")

    
    head = Node(0,None)
    iter = head
    for i in range(1,10):
        iter.next = Node(i,None)
        iter = iter.next
    print_linked_list(head)
    reversed_head = reverse_linked_list(head)
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()

