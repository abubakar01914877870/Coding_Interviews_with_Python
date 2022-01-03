if __name__ == "__main__":

    s = 'aba'
    n = 10


    def repeatedString(s, n):
        from collections import Counter
        s_count = Counter(s)
        len_s = len(s)
        in_div = n // len_s
        count_a1 = (s_count['a']) * in_div
        rm = n % len_s
        count_a2 = Counter(s[:rm])
        count_a2 = count_a2['a']
        total_count = count_a2 + count_a1
        return total_count




    print(repeatedString(s, n))
