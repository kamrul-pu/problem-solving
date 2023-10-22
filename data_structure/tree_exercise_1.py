"""Company Organogram using Tree."""


class TreeNode:
    def __init__(self, name: str, designation: str) -> None:
        self.name = name
        self.designation = designation
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

    def print_tree(self, data: str):
        spaces = " " * self.get_level() * 3
        if data == "both":
            txt = f"{self.name} ({self.designation})"
        elif data == "name":
            txt = self.name
        elif data == "designation":
            txt = self.designation
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + txt)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(data)


def build_organization_tree():
    root = TreeNode("Nilupul", "CEO")
    chinmoy = TreeNode("Chinmoy", "CTO")
    gels = TreeNode("Gels", "HR Head")
    vishwa = TreeNode("Vishwa", "Infrastructure Head")
    amir = TreeNode("Amir", "Application Head")
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abijhit", "App Manager"))
    chinmoy.add_child(vishwa)
    chinmoy.add_child(amir)
    gels.add_child(TreeNode("Peter", "Recruitement Manager"))
    gels.add_child(TreeNode("Waqes", "Policy Manager"))
    # Add to the root tree
    root.add_child(chinmoy)
    root.add_child(gels)

    return root


if __name__ == "__main__":
    root = build_organization_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
