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
        if iter.next and iter.next.val == val:
            iter.next = iter.next.next
            return dummy.next
        else:
            print(f"{val} does not exist in linked list")
            return head
    except Exception as e:
        print(f"An error occurred: {e}")
        return head
    
def main():
    arr = list(range(100000000))

    #Remove num time from array
    print("Array Removal")
    start_time = datetime.now()
    arr.remove(853)
    end_time = datetime.now()
    print(f"Execution time:{end_time - start_time}")


    #Populate our Linked List the same way

    head = Node(0,None)
    iter = head
    for i in range(1,100000000):
        iter.next = Node(i,None)
        iter = iter.next

    #Now remove same 853 from LinkedList

    print("Linked List Removal")
    start_time = datetime.now()
    remove_node(head,853)
    end_time = datetime.now()
    print(f"Execution time:{end_time - start_time}")

if __name__ == "__main__":
    main()

