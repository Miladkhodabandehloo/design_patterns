# https://sourcemaking.com/design_patterns/visitor/python/1
# http://www.newthinktank.com/2012/11/visitor-design-pattern-tutorial/
# The Visitor design pattern allows you to add methods to classes of different types without much altering to those classes. You can make completely different methods depending on the class used with this pattern.


class Visitable(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        pass


class Liquor(Visitable):
    def accept(self, visitor):
        return visitor.visit_liquor(self)


class Necessity(Visitable):
    def accept(self, visitor):
        return visitor.visit_necessity(self)


class Visitor(object):
    def visit(self):
        pass

    def visit_necessity(self, necessity):
        pass

    def visit_liquor(self, liquor):
        pass


class TaxVisitor(Visitor):
    def visit_necessity(self, necessity):
        return necessity.price * 0.05

    def visit_liquor(self, liquor):
        return liquor.price * 0.10


class HolidayTaxVisitor(Visitor):
    def visit_necessity(self, necessity):
        return necessity.price * 0.02

    def visit_liquor(self, liquor):
        return liquor.price * 0.05


red_wine = Liquor(name="red wine", price=20)
holiday_tax_visitor = HolidayTaxVisitor()
normal_tax_visitor = TaxVisitor()
print(red_wine.accept(visitor=holiday_tax_visitor))
print(red_wine.accept(visitor=normal_tax_visitor))
