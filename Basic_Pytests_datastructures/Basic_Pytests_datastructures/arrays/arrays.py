class MyArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_item_at_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]

    def size(self):
        return len(self.items)
