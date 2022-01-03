if __name__ == "__main__":
    haystack = ""
    needle = "a"

    def strStr(haystack, needle):
        import re
        if not haystack and not needle:
            return 0
        result = [(m.start(0), m.end(0)) for m in re.finditer(needle, haystack)]
        if not result:
            return -1
        else:
            return result[0][0]












    print(strStr(haystack, needle))
