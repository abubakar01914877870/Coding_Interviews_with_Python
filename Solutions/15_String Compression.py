if __name__ == "__main__":
    chars = ["a","a","a","b","b","a","a"]
  # https://leetcode.com/problems/string-compression/submissions/
    def compress(chars):
        n = len(chars)
        current_index = 1
        previous_chars = chars[0]
        count = 1

        i = 1
        while i < n:
            if chars[i] == previous_chars:
                count += 1
            else:
                if count > 1:
                    temp_s = str(count)
                    for ch in temp_s:
                        chars[current_index] = ch
                        current_index += 1
                previous_chars = chars[i]
                chars[current_index] = chars[i]
                current_index += 1
                count = 1
            i += 1
        if count > 1:
            temp_s = str(count)
            for ch in temp_s:
                chars[current_index] = ch
                current_index += 1
        return current_index









    print(compress(chars))
