if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"


    def isAnagram(s, t):
        from collections import Counter
        return Counter(s) == Counter(t)


    print(isAnagram(s, t))
