def validPalindrome(s):
    def checkPalindrome(low, high):
        i, j = low, high
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    res = s
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            if checkPalindrome(low + 1, high):
                res = s[:low] + s[low + 1:]
                return res
            if checkPalindrome(low, high - 1):
                res = s[:high] + s[high + 1:]
                return res
            return 'false'
    return res


s = input()
print(validPalindrome(s))
