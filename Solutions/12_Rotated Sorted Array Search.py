if __name__ == "__main__":
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 10

    def search_roated_array(A, B):
        new_array = []
        for i, j in enumerate(A):
            new_array.append((j, i))
        new_array.sort()
        #print(new_array)

        left, right = 0, len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if new_array[mid][0] == B:
                return new_array[mid][1]
            elif new_array[mid][0] < B:
                left = mid + 1
            else:
                right = mid - 1
        return -1




    print(search_roated_array(A, B))