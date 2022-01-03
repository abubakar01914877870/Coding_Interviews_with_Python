# https://leetcode.com/problems/sqrtx/
# https://www.interviewbit.com/problems/square-root-of-integer/


if __name__ == "__main__":
    x = 11


    def find_square_root(x):
        if x == 0 or x == 1:
            return x

        def search_sqrt(left, right):
            if left > right:
                return right
            if left == right:
                return left
            mid = (left + right) // 2
            current_value = mid * mid
            if current_value == x:
                return mid
            if current_value > x:
                return search_sqrt(left, mid - 1)
            if current_value < x:
                return search_sqrt(mid + 1, right)

        root = search_sqrt(1, x)
        if root * root > x:
            return root - 1
        return root


    print(find_square_root(x))
