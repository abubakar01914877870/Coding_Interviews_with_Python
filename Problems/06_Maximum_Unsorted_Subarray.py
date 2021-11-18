if __name__ == "__main__":
    A = [1, 2, 3, 5, 4]


    def subsort(A):
        n = len(A)
        B = sorted(A)
        i = 0
        start, end = -1, -1
        while i < n:
            if A[i] != B[i]:
                start = i
                break
            i += 1

        if start == -1:
            return [-1]
        j = n - 1

        while j >= 0:
            if A[j] != B[j]:
                end = j
                break
            j -= 1
        return [start, end]


    print(subsort(A))
