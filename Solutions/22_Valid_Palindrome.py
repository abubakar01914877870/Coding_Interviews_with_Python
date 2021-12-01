if __name__ == "__main__":
    import re
    s = "af"
    p = "be"



    def findAnagram(s, p):
        p_len = len(p)
        n = 0
        result = []

        while n + p_len < len(s)+1:
            for i in s[n:n+p_len]:
                chr_sum += ord(i)
            print(chr_sum)
            if chr_sum == p_aschi_sum:
                result.append(n)
            n += 1
        return result

        


    print(findAnagram(s, p))
