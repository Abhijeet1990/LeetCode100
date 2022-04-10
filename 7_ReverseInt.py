class Solution:
    def reverse(self, x):
        neg = False
        if str(x)[0] == '-':
            neg = True

        def result(x):
            counter, res = len(str(x)), 0
            while x > 0:
                y = x % 10
                x = x // 10
                res += y * (10 ** (counter - 1))
                counter -= 1
            if res >= 2 ** 31:
                return 0
            return res

        if neg:
            m = str(x)[1:]
            resn = result(int(m))
            if resn == 0:
                return 0
            else:
                return -int(str(resn))
        else:
            return result(x)
