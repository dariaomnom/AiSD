# string = list(input())
# N = list(map(int, string))
# while len(N) > 1:
#     sum_nums_str = str(sum(N))
#     N = list(map(int, list(sum_nums_str)))
# print(N[0])

# A = list(input())
# B = list(input())
# res = [0]
# cnt = 0
# dif = 0
# for i in range(len(B)-1, -1, -1):
#     cnt = dif
#     for j in range(len(A)-1, -1, -1):
#         a = int(A[j])
#         b = int(B[i])
#         res.append(0)
#         res[cnt] = res[cnt] + ((b * a) % 10)
#         res[cnt+1] = (b * a) // 10
#         print('res[cnt+1]',res[cnt+1])
#
#         print(a*b)
#         print('res[cnt]',res[cnt])
#         print()
#
#         cnt += 1
#     dif += 1
#
# print(res)
# res_ab = [0] * len(res)
# for i in range(0, len(res)):
#     res_ab[i] = res[0-(i+1)]
# print(*res_ab)



# A = list(input())
# B = list(input())
# A = A[::-1]
# B = B[::-1]
# res = [0] * (len(A) + len(B))
#
# for i in range(len(A)):
#     for j in range(len(B)):
#         res[i + j] += int(A[i]) * int(B[j])
#
# carry = 0
# for i in range(len(res)):
#     res[i] += carry
#     carry = res[i] // 10
#     res[i] %= 10
#
# while len(res) > 1 and res[-1] == 0:
#     res.pop()
#
# res = res[::-1]
#
# print(''.join(map(str, res)))



def check_brackets(expression):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for i, char in enumerate(expression, start=1):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack[-1][0]) != closing_brackets.index(char):
                return i
            stack.pop()

    if stack:
        return stack[0][1]
    else:
        return "Success"
# Примеры использования
# print(check_brackets("{[]}()"))  # Output: Success
# print(check_brackets("{"))  # Output: 1
# print(check_brackets("{[}"))
# print(check_brackets("()"))



# class Stack:
#     def __init__(self, value):
#         self.stack = [value]
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if self.isEmpty():
#             return 0
#         return self.stack.pop()
#
#     def isEmpty(self):
#         return len(self.stack) == 0

#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add(self, values):
#         for value in values:
#             new_node = Node(value)
#             if self.head is None:
#                 self.head = new_node
#                 self.tail = new_node
#             else:
#                 self.tail.next = new_node
#                 self.tail = new_node
#
#     def reverse(self):
#         prev_node = None
#         curr_node = self.head
#         while curr_node:
#             next_node = curr_node.next
#             curr_node.next = prev_node
#             prev_node = curr_node
#             curr_node = next_node
#         self.head = prev_node
#
#     def __str__(self):
#         curr = self.head
#         elements = []
#         while curr:
#             elements.append(str(curr.value))
#             curr = curr.next
#         return ' -> '.join(elements)
#
# # Example usage
# linked_list = LinkedList()
# linked_list.add([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
# linked_list.reverse()
# print(linked_list)  # Output: [6, 7, 8, 9] -> [4, 5] -> [1, 2, 3]

#
# import math
#
# class Node:
#     def __init__(self, n_array):
#         self.array = []
#         self.next = None
#
# class UnrolledLinkedList:
#     def __init__(self, n_array=4):
#         self.head = None
#         self.n_array = n_array
#
#     def insert(self, value, index):
#         if index < 0:
#             raise IndexError("Index out of range")
#
#         if self.head is None:
#             new_node = Node(self.n_array)
#             new_node.array.append(value)
#             self.head = new_node
#         else:
#             curr_node = self.head
#             while curr_node:
#                 if index <= len(curr_node.array):
#                     curr_node.array.insert(index, value)
#                     if len(curr_node.array) > curr_node.n_array:
#                         self.rebalance(curr_node)
#                     return
#                 index -= len(curr_node.array)
#                 if curr_node.next is None:
#                     new_node = Node(self.n_array)
#                     new_node.array.append(value)
#                     curr_node.next = new_node
#                     if len(new_node.array) > new_node.n_array:
#                         self.rebalance(new_node)
#                     return
#                 curr_node = curr_node.next
#
#     def delete(self, index):
#         if index < 0 or self.head is None:
#             raise IndexError("Index out of range")
#
#         curr_node = self.head
#         while curr_node:
#             if index < len(curr_node.array):
#                 value = curr_node.array.pop(index)
#                 if len(curr_node.array) < math.ceil(curr_node.n_array/2):
#                     self.rebalance(curr_node)
#                 return value
#             index -= len(curr_node.array)
#             prev_node = curr_node
#             curr_node = curr_node.next
#
#         raise IndexError("Index out of range")
#
#     def index(self, value):
#         curr_node = self.head
#         index = 0
#         while curr_node:
#             for i in range(len(curr_node.array)):
#                 if curr_node.array[i] == value:
#                     return index
#                 index += 1
#             curr_node = curr_node.next
#         raise ValueError("Value not found")
#
#     def print(self):
#         curr_node = self.head
#         elements = []
#         while curr_node:
#             elements.extend(curr_node.array)
#             curr_node = curr_node.next
#         print(*elements, sep=" ")
#
#     def rebalance(self, node):
#         if len(node.array) == node.n_array:
#             mid = node.n_array//2
#             new_node = Node(node.n_array)
#             new_node.array = node.array[mid:]
#             node.array = node.array[:mid]
#             new_node.next = node.next
#             node.next = new_node
#         elif len(node.array) < math.ceil(node.n_array/2) and node.next:
#             if len(node.array) + len(node.next.array) <= node.n_array:
#                 node.array.extend(node.next.array)
#                 node.next = node.next.next
#             else:
#                 deficit = math.ceil(node.n_array/2) - len(node.array)
#                 node.array.extend(node.next.array[:deficit])
#                 node.next.array = node.next.array[deficit:]
#
# # Example usage
# linked_list = UnrolledLinkedList()
# linked_list.insert(1, 0)
# linked_list.insert(2, 1)
# linked_list.insert(3, 1)
# linked_list.insert(4, 3)
# linked_list.insert(5, 0)
# linked_list.insert(6, 2)
#
# linked_list.print()  # Output: 5 1 6 3 2 4
#
# linked_list.delete(2)
# linked_list.print()  # Output: 5 1 3 2 4

#
# class Node:
#     def __init__(self, n_array):
#         self.array = [None]*n_array
#         self.next = None
#         self.length = 0
#
# class UnrolledLinkedList:
#     def __init__(self, n_array=4):
#         self.head = Node(n_array)
#         self.n_array = n_array
#
#     def insert(self, element, index=-1):
#         node = self.head
#         if index < 0:
#             index = self.length + 1 + index
#         while node is not None:
#             for i in range(self.n_array):
#                 if node.array[i] is None or i == index:
#                     node.array[i] = element
#                     return
#                 if node.next is None:
#                     node.next = Node(self.n_array)
#             node = node.next
#
#     def delete(self, index):
#         node = self.head
#         while node is not None:
#             for i in range(self.n_array):
#                 if i == index:
#                     node.array[i] = None
#                     return
#             node = node.next
#
#     def index(self, element):
#         node = self.head
#         idx = 0
#         while node is not None:
#             for i in range(self.n_array):
#                 if node.array[i] == element:
#                     return idx
#                 idx += 1
#             node = node.next
#         return -1
#
#     def print(self):
#         node = self.head
#         while node is not None:
#             for i in range(self.n_array):
#                 if node.array[i] is not None:
#                     print(node.array[i], end=' ')
#             node = node.next
#         print()
#
# linked_list = UnrolledLinkedList()
# for i in range(10):
#     linked_list.insert(i)
# # linked_list.insert(1)
# linked_list.print()
# linked_list.delete(7)
# linked_list.print()

class Node:
    def __init__(self):
        self.arr = []
        self.next = None

class UnrolledLinkedList:
    def __init__(self, n_array=4):
        self.head = None
        self.len = 0
        self.n_array = n_array

    def insert(self, elem, index=-1):
        # if index >= self.len:
        #     index = -1
        # if index < 0:
        #     index = self.len + index
        if self.head is None:
            self.head = Node()
            self.head.arr.append(elem)
            # print(elem)
            self.len += 1
            return
        else:
            self.len += 1
            if index >= self.len:
                index = self.len - 1
            if index < 0:
                index = self.len + index

            node = self.head
            # cnt = 0
            # while node is not None:
            #     cnt += 1
            #     if cnt * self.n_array > index:
            #         if len(node.arr) <= (index % ) and len(node.arr) < self.n_array:
            #             node.arr.insert(elem, index)
            #     node = node.next
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
                node.arr = arr_to_split[:self.n_array//2+1]
                new_node.arr = arr_to_split[self.n_array//2+1:]
            # while node is not None:
            #
            #     if len(node.arr) < self.n_array:
            #         node.arr.append(elem)
            #     else
            #     node = node.next
            # self.len += 1

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
            # print(index, tmp_index)
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

    def print(self):
        node = self.head
        while node is not None:
            print(node.arr)
            node = node.next

        node = self.head
        while node is not None:
            for i in range(len(node.arr)):
                print(node.arr[i], end=' ')
            # print(node.arr)
            node = node.next

ll = UnrolledLinkedList(4)
ll.insert(5)
ll.insert(33, 100)
ll.insert(51, 0)
ll.insert(73, 0)
ll.insert(92, 0)
ll.print()
print()
# ll.delete(5)
# ll.delete(2)
# ll.print()
# print()

print(ll.index(73))

# linked_list = UnrolledLinkedList()
# linked_list.insert(5, 0)
# linked_list.insert(1, 1)
# linked_list.insert(3, 2)
# linked_list.insert(7, 3)
# linked_list.insert(2, 4)
# # linked_list.insert(9, 5)
# # linked_list.insert(16, 6)
# linked_list.insert(100, 3)
# linked_list.insert(200, 3)
# linked_list.insert(50, 5)
# linked_list.print()
# print()
#
# linked_list.delete(5)
# linked_list.delete(4)
# linked_list.delete(3)
# linked_list.print()
# print()
#
# linked_list.insert(67,3)
# linked_list.insert(45,3)
# linked_list.print()