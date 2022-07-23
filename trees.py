class TreeNode:
    def __init__(self, name, designation):
        self.data = name, designation
        self.children = []
        self.parent = None
        print(self.children)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, value):
        space = ' ' * self.get_level() * 3
        prefix = "|__" if self.get_level() > 0 else ""
        if value == "both":
            print(space + prefix + self.data[0] + self.data[1])
        elif value == "name":
            print(space + prefix + self.data[0])
        else:
            print(space + prefix + self.data[1])
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(value)


def build_product_tree():
    root = TreeNode("Nilupul", "(CEO)")

    level_1 = TreeNode("Chinmay", "(CTO)")
    level_2 = TreeNode("Vishwa", "(Infrastructure head)")
    level_22 = TreeNode("Aamir", "(Application Head)")
    level_1.add_child(level_2)
    level_1.add_child(level_22)
    level_3 = TreeNode("Dhaval", "(Cloud Manager)")
    level_33 = TreeNode("Abhiji", "(App Manager)")
    level_2.add_child(level_3)
    level_2.add_child(level_33)

    level_11 = TreeNode("Gels", "(HR Head)")
    level_11.add_child(TreeNode("Peter", "(Recruitment Manager)"))
    level_11.add_child(TreeNode("Waqas", "(Policy Manager)"))

    root.add_child(level_1)
    root.add_child(level_11)


    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree(value="both")
