if __name__ == "__main__":
    A = [5, -2, 3 , 1, 2]
    B = 3

    def solve(A, B):
        res = sum(A[:B])
        print(A[:B])
        summ = res
        for i in range(B):
            summ = summ - A[B - 1 - i]
            print(A[B - 1 - i])
            print(A[len(A) - 1 - i])
            summ = summ + A[len(A) - 1 - i]
            res = max(res, summ)
        return res



    print(solve(A,B))