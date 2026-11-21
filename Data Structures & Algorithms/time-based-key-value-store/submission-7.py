class TimeMap:

    def __init__(self):
        self.table=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table.keys():
            return ""
        l,r=0,len(self.table[key])-1
        pair=self.table[key]
        res=""
        while l<=r:
            mid = l + (r-l)//2
            if pair[mid][0]<=timestamp:
                res=pair[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
