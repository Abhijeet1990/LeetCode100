class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        store = []
        for i in range(numRows):
            inner = []
            store.append(inner)
        k = 0
        inc = True
        for i,ch in enumerate(s):
            store[k].append(ch)
            if k == numRows-1:
                inc = False
            elif k == 0:
                inc = True
            if inc:
                k+=1
            else:
                k-=1
        res=''
        for ele in store:
            for ch in ele:
                res+=ch
        return res