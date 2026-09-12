#  Problem: https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                n -= 1

        else:
            for i in range (len(flowerbed)):
                if i == 0:
                    if flowerbed[i] == 1:
                        continue
                    else:
                        if flowerbed[i+1] == 1:
                            continue
                        else:
                            flowerbed[i] = 1
                            n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i] == 1:
                        continue
                    else:
                        if flowerbed[i-1] == 1:
                            continue
                        else:
                            flowerbed[i] = 1
                            n-= 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed [i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1

        if n <= 0:
            return True
        else:
            return False       
