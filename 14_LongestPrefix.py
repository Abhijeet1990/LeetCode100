class Solution:
    def longestCommonPrefix(self, strs):
        first = strs[0]
        val=[]
        for str in strs:
            ctr=0
            for i in range(min(len(first),len(str))):
                if str[i] == first[i]:
                    ctr+=1
                else:
                    break
            val.append(ctr)
        x = min(val)
        return first[:x]