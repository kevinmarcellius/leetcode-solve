# move-zeroes
# Problem: https://leetcode.com/problems/move-zeroes/submissions/2142842913/?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx_zero = -1
        idx_non_zero = 0

        for i in range (len(nums)):
            if nums[i] == 0:
                if idx_non_zero == 0:
                    idx_non_zero = i
                    
                for j in range (idx_non_zero, len(nums)):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        idx_non_zero = j
                        break

        return nums

# a better approach from other users submission:
j = 0

for i in range (len(nums)):
	if nums[i] != 0:
		nums[i], nums[j] = nums[j], nums[i]
                j += 1

# reasoning:
# there are 2 conditions: 0 followed by non 0, and 0 followed by 0
# suppose j is the current index of 0, or we can say, the current place to put the non 0, 
# simply add 1 to j after swapping. because the next number after current j will always be 0 (either 0 after swapping or it already is 0
