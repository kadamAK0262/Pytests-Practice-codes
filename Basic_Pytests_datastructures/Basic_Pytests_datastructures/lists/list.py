class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def remove(self, item):
        self.items.remove(item)

    # def pop(self, index=None):
    #     return self.items.pop(index)

    def pop(self, index=None):
        if index is not None:
            return self.items.pop(index)
        elif self.items:
            return self.items.pop()
        else:
            raise IndexError("pop from empty list")

    def count(self, item):
        return self.items.count(item)

    def clear(self):
        self.items.clear()

    def reverse(self):
        self.items.reverse()

    def extend(self, iterable):
        self.items.extend(iterable)
