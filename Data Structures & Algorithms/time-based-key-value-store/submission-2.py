class TimeMap:

    def __init__(self):
        self.timemap = {None: None} # Key: (value,stamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap.keys():
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        getter = ""
        if key not in self.timemap.keys():
            return getter
        searchlist = self.timemap[key]
        l = 0
        r = len(searchlist) -1

        while l <= r:
            m = (l + r)//2
            if searchlist[m][1] <= timestamp:
                getter = searchlist[m][0]
                l = m+1
            else:
                r = m -1
        return getter

        
