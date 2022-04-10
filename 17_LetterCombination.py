class Solution:
    def letterCombinations(self, digits):
        map ={'1':[],'2':['a','b','c'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[]
        def combine(num,origList):
            res=[]
            for i in map[num]:
                for k in origList:
                    res.append(k+i)
            return res
        for j,ch in enumerate(digits):
            if ch in map:
                p=[]
                for i in map[ch]:
                    p.append(i)
                if j>=1:
                    res = combine(ch,res)
                if j == 0:
                    res = p
        return res