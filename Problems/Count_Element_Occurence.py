from typing import List

if __name__ == "__main__":
    A = s = ["h","e","l","l","o"]
    B = 9


    def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        m = n // 2

        for i in range(m):
            s[i], s[n-1-i] = s[n-1-i], s[i]
        print(
                s
                )

    reverseString(A)