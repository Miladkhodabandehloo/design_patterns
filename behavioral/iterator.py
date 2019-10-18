class MyIterator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        output = self.a
        if output > 100:
            raise StopIteration
        self.a = self.a + 2
        return output


for i in MyIterator():
    print(i)
