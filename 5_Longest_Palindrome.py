class Solution:
    def longestPalindrome(self, s):
        if s == None or len(s) == 0:
            return ''
        start, end = 0, 0
        for i, ch in enumerate(s):
            l1 = self.expAroundCenter(s, i, i)
            # print(l1)
            l2 = self.expAroundCenter(s, i, i + 1)
            # print(l2)
            lm = max(l1, l2)
            if (lm > (end - start)):
                start = i - (lm - 1) // 2
                end = i + lm // 2
        print('start ', start, ' end ', end)
        return s[int(start):int(end + 1)]

    def expAroundCenter(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return r - l - 1