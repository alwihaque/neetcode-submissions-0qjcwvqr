class TimeMap:

    def __init__(self):
        self.hm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = (value, timestamp)
        self.hm[key] = self.hm.get(key, []) + [val]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        val = self.hm[key]
        # in sorted order
        if timestamp > val[-1][1]:
            return val[-1][0]
        # otherwise do binary search
        l, r = 0, len(val) - 1
        prev_ts_val = ""
        while l <= r:
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                prev_ts_val = val[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return prev_ts_val

        
            
        
