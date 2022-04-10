class Solution:
    def generateParenthesis(self, n):
        res=[]
        pstack = [('',n,n)]
        # the length of each component will be 2n
        while pstack:
            ele, l, r = pstack.pop()
            if not l and not r:
                res.append(ele)
            else:
                if l:
                    pstack.append((ele+'(', l-1,r))
                if r-1>=l:
                    pstack.append((ele+')',l,r-1))
        return res