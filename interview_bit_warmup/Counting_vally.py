if __name__ == "__main__":

    ar = "UDUUUDUDDD"
    ar2 = "UDDDUDUU"
    ar3 = 'DDUUDDUDUUUD'

    def countingValleys(steps, path):
        new_path = path[::-1]
        l_path = list(new_path)
        print(l_path)
        ground = 0
        vally_count = 0
        enter_vally = False
        while len(l_path) > 0:
            current_step = l_path.pop()
            if current_step== 'U':
                ground += 1
            if current_step == 'D':
                ground -= 1
            if ground < 0:
                enter_vally = True
            if ground == 0 and enter_vally:
                vally_count += 1
                enter_vally = False
        return vally_count


    print(countingValleys(8, ar))
