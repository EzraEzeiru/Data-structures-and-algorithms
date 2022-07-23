# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.right = None
#         self.left = None
#
#
# node = TreeNode(key=3)
# node1 = TreeNode(key=4)
# node2 = TreeNode(key=5)
#
# node.right = node1
# node.left = node2

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


# def parse_tuple(data):
#     if isinstance(data, tuple) and len(data) == 3:
#         node = TreeNode(data[1])
#         node.left = parse_tuple(data[0])
#         node.right = parse_tuple(data[2])
#
#     elif data == None:
#         node = None
#
#     else:
#         node = TreeNode(data)


# HASH TABLES IN PYTHON

MAX_HASH_TABLE_SIZE = 4096


def get_index(data_list, key):
    result = 0

    for char in key:
        char_number = ord(char)
        result += char_number

    idx = result % len(data_list)
    return idx


class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        index = get_index(self.data_list, key)
        self.data_list[index] = (key, value)

    def find(self, key):
        index = get_index(self.data_list, key)
        kv = self.data_list[index]
        if kv is None:
            return None

        else:
            key, value = kv
            return value

    def update(self, key, value):
         index = get_index(self.data_list, key)
         self.data_list[index] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


def get_valid_index(data_list, key):
    idx = get_index(data_list, key)

    while True:
        kv = data_list[idx]

        if kv is None:
            return idx

        k, v = kv
        if key == kv[0]:
            return idx

        idx += 1

        if idx == len(data_list):
            idx = 0

data_list2 = [None] * MAX_HASH_TABLE_SIZE

if get_valid_index(data_list2, 'listen') == 655:
    print(True)

data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

print(get_valid_index(data_list2, 'silent'))


