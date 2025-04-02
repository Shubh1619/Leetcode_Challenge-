s="abcabcbb"

def lengthOfLongestSubstring(self,s) :
    char_set = set()
    left = 0
    ans = 0

    for i in range(len(s)):
        while s[i] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[i])
        ans = max(ans, i - left + 1)

    return ans
print(lengthOfLongestSubstring(0,s))