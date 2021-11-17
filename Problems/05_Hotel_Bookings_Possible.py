if __name__ == "__main__":
    A = [1, 3, 5]
    B = [2, 6, 8]
    C = 2


    def hotel(arrive, depart, K):
        n = len(arrive)
        arrive.sort()
        depart.sort()

        count = 0
        i, j = 0, 0
        while i < n and j < n:
            if arrive[i] < depart[j]:
                count += 1
                i += 1
                if count > K:
                    return False
            else:
                count -= 1
                j += 1
        return True

    print(hotel(A, B, C))
