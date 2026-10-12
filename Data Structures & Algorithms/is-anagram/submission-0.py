class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if dict1.get(i):
                dict1.update({i:dict1.get(i)+1})
            else:
                dict1.update({i:1})
        for j in t:
            if dict2.get(j):
                dict2.update({j:dict2.get(j)+1})
            else:
                dict2.update({j:1})
        print(dict1)
        print(dict2)
        return dict1 == dict2