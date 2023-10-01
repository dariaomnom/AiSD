
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
                node.arr = arr_to_split[:self.n_array//2]
                new_node.arr = arr_to_split[self.n_array//2:]

            # self.n_array % 2
            # не надо
            # while len(node.arr) > self.n_array:
            #     if node.next:
            #         while len(node.arr) > self.n_array // 2 + self.n_array % 2:
            #             node.next.arr.insert(0, node.arr.pop())
            #     else:
            #         node.next = Node()
            #         while len(node.arr) > self.n_array // 2 + self.n_array % 2:
            #             node.next.arr.insert(0, node.arr.pop())
            #     node = node.next
            # не надо

            # не стоит использовать
            # while len(node.arr) > self.n_array:
            #     # if node.next is not None and len(node.arr) > self.n_array // 2 + self.n_array % 2:
            #     if node.next is not None and len(node.arr) > self.n_array:
            #         to_replace = node.arr.pop()
            #         node.next.arr.insert(0, to_replace)
            #     # elif len(node.arr) > self.n_array // 2 + self.n_array % 2:
            #     elif len(node.arr) > self.n_array:
            #         node.next = Node()
            #         to_replace = node.arr.pop()
            #         node.next.arr.insert(0, to_replace)
            #     node = node.next
            # не стоит использовать

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
                # print('1 !!!', tmp_index, len(node.arr))
                tmp_index -= len(node.arr)
                prev_node = node
                node = node.next
            # print('2 !!!',index, tmp_index, 'elem', node.arr[tmp_index])
            deleted = node.arr.pop(tmp_index)
            self.len -= 1
            if len(node.arr) == 0:
                prev_node.next = node.next
                if len(self.head.arr) == 0:
                    self.head = self.head.next


        # while len(node.arr) < self.n_array and node.next is not None:
        #     # if node.next is not None:
        #     if len(node.arr) == 0:
        #         prev_node.next = node.next
        #         if len(self.head.arr) == 0:
        #             self.head = self.head.next
        #     elif len(node.next.arr) != 0:
        #         to_replace = node.next.arr.pop(0)
        #         node.arr.append(to_replace)
        #         node = node.next

        # if len(node.arr) == 0:
        #     prev_node.next = node.next
        #     if len(self.head.arr) == 0:
        #         self.head = self.head.next

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
        # node = self.head
        # while node is not None:
        #     print(node.arr, end=' ')
        #     node = node.next

        node = self.head
        string = ''
        while node is not None:
            for i in range(len(node.arr)):
                # print(node.arr[i], end=' ')
                string += str(node.arr[i]) + ' '
            # print(node.arr)
            node = node.next
        # print()
        print(string[:-1])

def check(arr1, arr2, n_array = 4):
    linked_list = UnrolledLinkedList(n_array)

    for i in arr1:
        linked_list.insert(i)
        linked_list.print()

    for i in arr2:
        linked_list.delete(linked_list.index(i))
        linked_list.print()
    return linked_list

check([0,1,2,3,4,5,6,7], [1,3,5,7]).print()

# ll = UnrolledLinkedList(6)
# for i in range(10):
#     ll.insert(i)
#     # ll.print()
#     # print()
# ll.print()
# print()
# print()
# for i in range(3,10):
#     ll.delete(i)
#     ll.print()
#     print()

# ll2 = UnrolledLinkedList()
# print(ll2.index(5))

