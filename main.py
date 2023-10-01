class Node:
    def __init__(self):
        self.arr = []
        self.next = None

class UnrolledLinkedList:
    def __init__(self, n_array = 4):
        self.head = None
        self.len = 0
        self.n_array = n_array

    def insert(self, elem, index=-1):
        if self.head is None:
            self.head = Node()
            self.head.arr.append(elem)
            self.len += 1
            return
        else:
            self.len += 1
            if index >= self.len:
                index = self.len - 1
            if index < 0:
                index = self.len + index

            node = self.head
            tmp_index = index
            while (node.next is not None) and (tmp_index > len(node.arr)):
                tmp_index -= len(node.arr)
                node = node.next
            node.arr.insert(tmp_index, elem)

            if len(node.arr) > self.n_array:
                new_node = Node()
                new_node.next = node.next
                node.next = new_node
                arr_to_split = node.arr
                node.arr = arr_to_split[:self.n_array//2]
                new_node.arr = arr_to_split[self.n_array//2:]


    def delete(self, index):
        deleted = None
        node = self.head
        prev_node = self.head
        if index >= self.len:
            index = -1
        if index < 0:
            index = self.len + index
        if node is not None and self.len > 0:
            tmp_index = index
            while (node.next is not None) and (tmp_index >= len(node.arr)):
                tmp_index -= len(node.arr)
                prev_node = node
                node = node.next
            deleted = node.arr.pop(tmp_index)
            self.len -= 1
            if len(node.arr) == 0:
                prev_node.next = node.next
                if len(self.head.arr) == 0:
                    self.head = self.head.next
        return deleted

    def index(self, elem):
        node = self.head
        cnt = 0
        while node is not None:
            for i in range(len(node.arr)):
                if node.arr[i] == elem:
                    return cnt
                cnt += 1
            node = node.next
        return "Not found"

    def print_elements(self):
        if self.head is None:
            return 'No elements'
        node = self.head
        string = ''
        while node is not None:
            for i in range(len(node.arr)):
                string += str(node.arr[i]) + ' '
            node = node.next
        print(string[:-1])

    def __str__(self):
        if self.head is None:
            return 'No elements'
        node = self.head
        string = ''
        while node is not None:
            string += str(node.arr) + ' '
            node = node.next
        return string[:-1]

def check(arr1, arr2, n_array = 4):
    linked_list = UnrolledLinkedList(n_array)

    for i in arr1:
        linked_list.insert(i)
        print(linked_list)

    for i in arr2:
        linked_list.delete(linked_list.index(i))
        print(linked_list)

    return linked_list
