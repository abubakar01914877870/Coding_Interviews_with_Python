if __name__ == "__main__":
    A = [5, -2, 3 , 1, 2]
    B = 3

    def solve(A, B):
        n = len(A)
        result = -1000000
        i = B
        j = 0
        while i >= 0:
            prefix_sum = sum(A[0:i])
            i -= 1
            safix_sum = sum(A[n-j:n])
            j += 1
            if result < prefix_sum + safix_sum:
                result = prefix_sum + safix_sum
        return result


    print(solve(A,B))