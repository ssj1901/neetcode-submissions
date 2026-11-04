class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        opening = {'(','{','['}
        closing = {')','}',']'}
        for c in s:
            if len(arr)==0:
                if c in closing:
                    return False
                else:
                    arr.append(c)
            else:
                if c in opening:
                    arr.append(c)
                else:
                    last = arr.pop()
                    if last == '(' and c ==')' or last == '{' and c == '}' or last == '[' and c == ']':
                        continue
                    else:
                        return False

        return len(arr)==0

