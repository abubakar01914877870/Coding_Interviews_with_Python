if __name__ == "__main__":
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]

    def spral_order(matrix):
        spiral_matrix = []

        m = len(matrix) # row
        n = len(matrix[0]) # column

        direction = 0

        left = 0
        right = n - 1

        top = 0
        bottom = m - 1

        while len(spiral_matrix) < m * n:
            # left to right
            if direction == 0:
                for i in range(left, right + 1):
                    print(matrix[top][i])
                    spiral_matrix.append(matrix[top][i])
                top += 1

            # top to bottom
            elif direction == 1:
                for i in range(top, bottom + 1):
                    print(matrix[i][right])
                    spiral_matrix.append(matrix[i][right])
                right -= 1

            # right to left
            elif direction == 2:
                for i in range(right, left -1, -1):
                    print(matrix[bottom][i])
                    spiral_matrix.append(matrix[bottom][i])
                bottom -= 1

            # bottom to top
            else:
                for i in range(bottom, top - 1, -1):
                    print(matrix[i][left])
                    spiral_matrix.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4
        return spiral_matrix

    spral_order(mat)
