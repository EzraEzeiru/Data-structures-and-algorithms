class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_elements(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        linked_list = ""
        while itr:
            linked_list += str(itr.data) + "----->"
            itr = itr.next

        print(linked_list)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next :
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index == 0 or index > self.get_length():
            raise Exception("Invalid index")

        elif index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data_to_insert)
                return

            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                self.remove(count)
                return

            itr = itr.next
            count += 1

        if itr is None:
            print("Value does not exist")
            return

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_after_value("mango", "apple")
    ll.remove_by_value("apple")
    ll.insert_at_end("pear")
    ll.print_elements()
    print(ll.get_length())
