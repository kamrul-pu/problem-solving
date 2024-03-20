"""Global COuntry Hirearchy."""


class TreeNode:
    def __init__(self, data) -> None:
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

    def print_tree(self, lvl: int):
        if self.get_level() > lvl:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(lvl)


def build_location_data():
    root = TreeNode("Global")
    bd = TreeNode("BD")
    usa = TreeNode("USA")

    dhaka = TreeNode("Dhaka")
    ctg = TreeNode("Chittagong")
    dhaka.add_child(TreeNode("Banani"))
    dhaka.add_child(TreeNode("Gulshan"))

    ctg.add_child(TreeNode("GEC"))
    ctg.add_child(TreeNode("Agrabad"))

    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Fransisco"))
    california.add_child(TreeNode("Mountain View"))

    bd.add_child(dhaka)
    bd.add_child(ctg)

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(bd)
    root.add_child(usa)
    return root


if __name__ == "__main__":
    root = build_location_data()
    root.print_tree(lvl=3)
