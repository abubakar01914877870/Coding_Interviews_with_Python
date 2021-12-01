if __name__ == "__main__":
    A = [1, 2, 3]
    B = [2, 5, 5]

    C = [[1,3],[6,9]]
    D = [2, 5]



    def isAnagram(A, B):
        array1 = int(''.join([str(i) for i in A]))
        array2 = int(''.join([str(i) for i in B]))
        result = str(array1 + array2)
        result = [int(i) for i in result]
        return result


    print(isAnagram(A, B))
