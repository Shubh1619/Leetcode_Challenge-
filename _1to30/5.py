def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    start, max_length = 0, 0

    for i in range(len(s)):
        # Check for odd-length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1

        # Check for even-length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1

    return s[start:start + max_length]

# Example usage
if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))  # Output: "bab" or "aba"