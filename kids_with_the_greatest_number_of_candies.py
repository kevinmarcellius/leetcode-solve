# Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = 0
        for i in candies:
            if i >= max_candy:
                max_candy = i
        result = []
        for i in candies:
            if i + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result
        


