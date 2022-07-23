class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

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

    def print_tree(self, level):
        space = " " * self.get_level() * 3
        prefix = "|__" if self.get_level() > 0 else ""
        print(space + prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                if child.get_level() > level:
                    break
                else:
                    child.print_tree(level)



def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    in_india1 = TreeNode("Gujarat")
    in_india2 = TreeNode("Karnataka")

    india.add_child(in_india1)
    india.add_child(in_india2)

    in_india1.add_child(TreeNode("Ahmedabad"))
    in_india1.add_child(TreeNode("Baroda"))

    in_india2.add_child(TreeNode("Bangluru"))
    in_india2.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")
    in_usa1 = TreeNode("New Jersey")
    in_usa2 = TreeNode("California")

    usa.add_child(in_usa1)
    usa.add_child(in_usa2)

    in_usa1.add_child(TreeNode("Princeton"))
    in_usa1.add_child(TreeNode("Trenton"))

    in_usa2.add_child(TreeNode("San Francisco"))
    in_usa2.add_child(TreeNode("Mountain View"))
    in_usa2.add_child(TreeNode("Palo Alto"))

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root = build_location_tree()
    root.print_tree(1)


