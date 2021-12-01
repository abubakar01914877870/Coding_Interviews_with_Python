if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8


    def search_range(nums, target):
        n = len(nums)
        result = []
        i = 0
        while i < n:
            if nums[i] == target:
                result.append(i)
            elif nums[i] < target:
                pass
            else:
                break
            i += 1

        if len(result) == 0:
            return [-1, -1]
        else:
            return [min(result), max(result)]


    print(search_range(nums, target))
