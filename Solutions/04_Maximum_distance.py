if __name__ == "__main__":
    A = [3, 5, 4, 2]

    def max_distance(A):
        number = []

        for i, num in enumerate(A):
            number.append((num, i))
        number.sort()
        max_gap = 0
        min_num = number[0][1]
        for item in number:
            num = item[1]
            if num <= min_num:
                min_num = num
            else:
                max_gap = max(max_gap, num, min_num)

        return max_gap

    print(max_distance(A))