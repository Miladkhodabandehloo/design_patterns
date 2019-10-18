import copy


class Prototype:
    def clone(self):
        return copy.copy(self)


class Pawn(Prototype):
    def __init__(self):
        self.name = "pawn"


class ChessItemFactory:

    def __init__(self):
        self.pawn = Pawn()

    def get_pawn(self):
        return self.pawn.clone()


item_factory = ChessItemFactory()

p1 = item_factory.get_pawn()
p2 = item_factory.get_pawn()
p2.name = "super pawn"

print(p1.name, p2.name, id(p1), id(p2))
