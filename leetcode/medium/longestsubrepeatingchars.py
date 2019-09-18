def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch]+1)
            dic[ch] = i

        return max(res, len(s)-start)




s = "stpedqzndgycukefnmgyxlpimgaeivhcowhuoijrrhuntasgmagjmwractemolpfkwzaeiuxro"
print(lengthOfLongestSubstring(s))