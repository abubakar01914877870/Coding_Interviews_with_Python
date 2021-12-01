if __name__ == "__main__":
    s = "fa"
    p = "ab"

    def findAnagram(s, p):
        p_len = len(p)
        p = sorted(p)
        n = 0
        result = []
        while n + p_len < len(s) + 1:
            if sorted(s[n:n+p_len]) == p:
                result.append(n)
            n += 1
        return result


print(findAnagram(s, p))

        