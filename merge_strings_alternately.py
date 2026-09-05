# Problem: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# Level: Easy
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        short = 0
        long_word = ""
        result = ""
        if len(word1) < len(word2):
            short = len(word1)
            long_word = word2
        else: 
            short = len(word2)
            long_word = word1
        
        for i in range (0, short):
            result += word1[i] + word2[i]
        
        if len(word1) != len(word2):
            result += long_word[short:]

        return result
