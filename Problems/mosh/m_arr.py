import arr

if __name__ == "__main__":
    A = arr.Array()
    A.insert(12)
    A.insert(11)
    A.insert(33)
    print(A.get_item_index(12))
    print(A.get_item_index(100))

    A.print()
