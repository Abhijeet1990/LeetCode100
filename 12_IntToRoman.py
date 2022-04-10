class Solution:
    def intToRoman(self, num: int) -> str:
        counter = 0
        res = ''

        def returnString(c, rem):
            map = {0: ('I', 'IV', 'IX', 'V'), 1: ('X', 'XL', 'XC', 'L'), 2: ('C', 'CD', 'CM', 'D')}
            if c < 3:
                if rem < 5:
                    if rem == 4:
                        return map[c][1]
                    else:
                        return rem * map[c][0]
                else:
                    if rem == 9:
                        return map[c][2]
                    else:
                        return map[c][3] + (rem - 5) * map[c][0]
            else:
                return rem * 'M'

        while num > 0:
            rem = num % 10
            num = num // 10
            res = returnString(counter, rem) + res
            counter += 1
        return res
