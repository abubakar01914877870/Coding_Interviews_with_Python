if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]


    def max_sub_array(nums):
        max_sum = nums[0]
        current_sum = 0

        num_len = len(nums)

        if num_len == 1:
            return nums[0]

        for i in range(num_len):
            current_sum = current_sum + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum


    print(max_sub_array(nums))
