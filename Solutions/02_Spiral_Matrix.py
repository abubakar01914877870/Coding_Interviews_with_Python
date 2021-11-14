if __name__ == "__main__":
    matrix = []

    def spiralOrder(matrix):
        spiral_order = []
        if len(matrix) == 0:
            return spiral_order
        m = len(matrix)  # Row
        n = len(matrix[0])  # Column

        direction = 0

        left = 0
        right = n - 1

        top = 0
        bottom = m - 1

        while len(spiral_order) < m * n:

            # Left to right
            if direction == 0:
                for i in range(left, right + 1):
                    spiral_order.append(matrix[top][i])
                top += 1

            # Top to bottom
            elif direction == 1:
                for i in range(top, bottom + 1):
                    spiral_order.append(matrix[i][right])
                right -= 1

            # Right to left
            elif direction == 2:

                for i in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to top
            else:
                for i in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4
        return spiral_order


    print(spiralOrder(matrix))
