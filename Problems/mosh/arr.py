class Array:
    def __init__(self):
        self.a = []

    def print(self):
        [print(i) for i in self.a]

    def insert(self, number):
        self.a.append(number)

    def remove(self, index):
        if 0 <= index < len(self.a):
            return self.a.pop(index)
        else:
            return -1

    def get_item_from_index(self, index):
        if index < len(self.a):
            return self.a[index]
        else:
            return -1

    def get_item_index(self, number):
        for i in range(len(self.a)):
            if self.a[i] == number:
                return i
        return -1

