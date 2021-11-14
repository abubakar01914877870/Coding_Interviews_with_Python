if __name__ == "__main__":
    L = [1, 1, 2, 2, 2, 33, 33]


    def removeDuplicates(nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            n = len(nums)
            # current_unique = nums[0]
            j = 1
            for i in range(1, n):
                if nums[i] != nums[i - 1]:
                    # current_unique = nums[i]
                    nums[j] = nums[i]
                    j += 1
            return j


    removeDuplicates(L)
