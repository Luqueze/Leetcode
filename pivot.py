class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Check if the left sum equals the right sum
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1


solution = Solution()
nums = [1, 7, 3, 6, 5, 6]
#print(solution.pivotIndex(nums))  