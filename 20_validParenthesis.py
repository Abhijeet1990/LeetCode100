class Solution:
    def isValid(self, s):
        map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i, ch in enumerate(s):
            if ch in map.keys():
                stack.append(ch)
            else:
                # this is an exception case if one brackets in the stack
                if not stack:
                    return False

                # remove every element stacked
                last_open = stack.pop()
                if map[last_open] != ch:
                    return False
        # if stack has been completely popped means it finds all closing brackets
        return not stack