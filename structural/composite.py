class Component:
    def __init__(self, name):
        self.name = name

    def info(self):
        pass


class Child(Component):

    def info(self):
        print(self.name)


class Composite(Child):
    def __init__(self, *args, **kwargs):
        super(Composite, self).__init__(*args, **kwargs)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def info(self):
        super(Composite, self).info()
        for child in self.children:
            child.info()


sub_menu1 = Child(name="mobile")
sub_menu2 = Child(name="lap top")
menu1 = Composite(name="electronic")
menu1.append_child(sub_menu1)
menu1.append_child(sub_menu2)
menu1.info()
