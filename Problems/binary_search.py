if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    B = 12


    def binary_search(A, B):
        new_A = []
        for i, j in enumerate(A):
            new_A.append([j, i])
        new_A.sort()
        left, right = 0, len(A)

        while left <= right:
            mid = (left + right) // 2

            if B == new_A[mid][0]:
                return new_A[mid][1]
            elif new_A[mid][0] < B:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    print(binary_search(A, B))
