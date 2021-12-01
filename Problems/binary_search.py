if __name__ == "__main__":
    A = [1, 1, 3, 3]


    def binary_search(A):
        A_len = len(A)
        A.sort()
        for i in range(A_len - 1):
            if A[i] <= A_len - 1 - i:
                return 1
        return -1


    print(binary_search(A))
