def lengthOfLongestSubstring(s) -> int:
    temp = []
    max_len = 1
    if s == '':
        return 0
    for ch in s:
        if ch not in temp:
            temp.append(ch)
        else:
            # get the index where there was repetition and remove all previous element
            i = temp.index(ch)
            temp = temp[(i + 1):]
            temp.append(ch)
        if len(temp) > max_len:
            max_len = len(temp)
    return max_len

print(lengthOfLongestSubstring('abhijeet'))