import time
from lb1 import *
import random

def time_test_unrolled_linked_list():
    print('Unrolled Linked List')
    print()

    linked_list = UnrolledLinkedList(20)

    # Test for inserting at the beginning
    start_time = time.time()
    for i in range(10):
        linked_list.insert(i, 0)
    print("10 Time for inserting at the beginning: ", time.time() - start_time)

    # start_time = time.time()
    # for i in range(1000):
    #     linked_list.insert(i, 0)
    # print("1 000 Time for inserting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        linked_list.insert(i, 0)
    print("10 000 Time for inserting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(100000):
        linked_list.insert(i, 0)
    print("100 000 Time for inserting at the beginning: ", time.time() - start_time)

    print()

    # Test for inserting at the end
    start_time = time.time()
    for i in range(10):
        linked_list.insert(i)
    print("10 Time for inserting at the end: ", time.time() - start_time)

    # start_time = time.time()
    # for i in range(1000):
    #     linked_list.insert(i)
    # print("1 000 Time for inserting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        linked_list.insert(i)
    print("10 000 Time for inserting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(100000):
        linked_list.insert(i)
    print("100 000 Time for inserting at the end: ", time.time() - start_time)

    print()

    # Test for inserting in the middle
    start_time = time.time()
    for i in range(10):
        linked_list.insert(i, linked_list.len // 2)
    print("10 Time for inserting in the middle: ", time.time() - start_time)

    # start_time = time.time()
    # for i in range(1000):
    #     linked_list.insert(i, linked_list.len // 2)
    # print("1 000 Time for inserting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        linked_list.insert(i, linked_list.len // 2)
    print("10 000 Time for inserting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(100000):
        linked_list.insert(i, linked_list.len // 2)
    print("100 000 Time for inserting in the middle: ", time.time() - start_time)

    print()

    # Test for deleting at the beginning
    start_time = time.time()
    for i in range(5):
        linked_list.delete(0)
    print("5 Time for deleting at the beginning: ", time.time() - start_time)

    # start_time = time.time()
    # for i in range(500):
    #     linked_list.delete(0)
    # print("500 Time for deleting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(5000):
        linked_list.delete(0)
    print("5 000 Time for deleting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(50000):
        linked_list.delete(0)
    print("50 000 Time for deleting at the beginning: ", time.time() - start_time)

    print()

    # Test for deleting at the end
    start_time = time.time()
    for i in range(5):
        linked_list.delete(-1)
    print("5 Time for deleting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(500):
        linked_list.delete(-1)
    print("500 Time for deleting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(5000):
        linked_list.delete(-1)
    print("5 000 Time for deleting at the end: ", time.time() - start_time)

    print()

    # Test for deleting in the middle
    start_time = time.time()
    for i in range(5000):
        linked_list.delete(linked_list.len // 2)
    print("5 Time for deleting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(500):
        linked_list.delete(linked_list.len // 2)
    print("500 Time for deleting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(5000):
        linked_list.delete(linked_list.len // 2)
    print("5 000 Time for deleting in the middle: ", time.time() - start_time)

    print()
    print()

def time_test_array():
    print('Array')
    print()

    arr = []

    # Test for inserting at the beginning
    start_time = time.time()
    for i in range(10):
        arr.insert(0, i)
    print("10 Time for inserting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(1000):
        arr.insert(0, i)
    print("1 000 Time for inserting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        arr.insert(0, i)
    print("10 000 Time for inserting at the beginning: ", time.time() - start_time)

    print()

    # Test for inserting at the end
    start_time = time.time()
    for i in range(10):
        arr.append(i)
    print("10 Time for inserting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(1000):
        arr.append(i)
    print("1 000 Time for inserting at the end: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        arr.append(i)
    print("10 000 Time for inserting at the end: ", time.time() - start_time)

    print()

    # Test for inserting in the middle
    start_time = time.time()
    for i in range(10):
        arr.insert(len(arr) // 2, i)
    print("10 Time for inserting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(1000):
        arr.insert(len(arr) // 2, i)
    print("1 000 Time for inserting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for i in range(10000):
        arr.insert(len(arr) // 2, i)
    print("10 000 Time for inserting in the middle: ", time.time() - start_time)

    print()

    # Test for deleting at the beginning
    start_time = time.time()
    for _ in range(5):
        del arr[0]
    print("5 Time for deleting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(500):
        del arr[0]
    print("500 Time for deleting at the beginning: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(5000):
        del arr[0]
    print("5 000 Time for deleting at the beginning: ", time.time() - start_time)

    print()

    # Test for deleting at the end
    start_time = time.time()
    for _ in range(5):
        arr.pop()
    print("5 Time for deleting at the end: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(500):
        arr.pop()
    print("500 Time for deleting at the end: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(5000):
        arr.pop()
    print("5 000 Time for deleting at the end: ", time.time() - start_time)

    print()

    # Test for deleting in the middle
    start_time = time.time()
    for _ in range(5):
        del arr[len(arr) // 2]
    print("5 Time for deleting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(500):
        del arr[len(arr) // 2]
    print("500 Time for deleting in the middle: ", time.time() - start_time)

    start_time = time.time()
    for _ in range(5000):
        del arr[len(arr) // 2]
    print("5 000 Time for deleting in the middle: ", time.time() - start_time)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_middle(self, data, position):
        new_node = Node(data)
        if position is None:
            print("The mentioned position is invalid")
            return
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is not None:
                current = current.next
        if current is None:
            print("The mentioned position is invalid")
        else:
            new_node.next = current.next
            current.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

def time_test_linked_list():
    print('Linked List')
    print()

    linked_list = LinkedList()

    # Test for inserting at the beginning
    start_time = time.time()
    for i in range(10000):
        linked_list.insert_beginning(i)
    print("Time for inserting at the beginning: ", time.time() - start_time)


    print()

    # Test for inserting at the end
    start_time = time.time()
    for i in range(10000):
        linked_list.insert_end(i)
    print("Time for inserting at the end: ", time.time() - start_time)

    print()

    # Test for inserting in the middle
    start_time = time.time()
    for i in range(10000):
        linked_list.insert_middle(i, linked_list.head.data // 2)
    print("Time for inserting in the middle: ", time.time() - start_time)

    print()

    # Test for deleting at the beginning
    start_time = time.time()
    for _ in range(5000):
        linked_list.delete_node(linked_list.head.data)
    print("Time for deleting at the beginning: ", time.time() - start_time)

    print()

    # Test for deleting at the end
    start_time = time.time()
    for _ in range(5000):
        node = linked_list.head
        while node.next is not None:
            prev_node = node
            node = node.next
        linked_list.delete_node(prev_node.data)
    print("Time for deleting at the end: ", time.time() - start_time)

    print()

    # Test for deleting in the middle
    start_time = time.time()
    for _ in range(5000):
        linked_list.delete_node(linked_list.head.data // 2)
    print("Time for deleting in the middle: ", time.time() - start_time)

    print()

time_test_unrolled_linked_list()
# time_test_array()
# time_test_linked_list()