# Problem: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# reverse_vowels_of_a_string

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = "aAiIuUeEoO"
        s_list = list(s)
        vowel_in_s = []
        for c in s:
            if c in vowel:
                vowel_in_s.append(c)

        x = 0
        for i in range (0, len(s)):
            if s[i] in vowel:
                s_list[i] = str(vowel_in_s[len(vowel_in_s) - x -1])
                x += 1
        
        return "".join(s_list)
