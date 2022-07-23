class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        left = self.left
        while left:
            if left.left is None:
                break
            left = left.left

        return left.data

    def find_max(self):
        right = self.right
        while right:
            if right.right is None:
                break
            right = right.right

        return right.data

    def calculate_sum(self):
       left_sum = self.left.calculate_sum() if self.left else 0
       right_sum = self.right.calculate_sum() if self.right else 0

       return self.data + left_sum + right_sum


    def delete_num(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_num(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_num(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.left is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_num(val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 2, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
