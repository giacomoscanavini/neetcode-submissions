class TimeMap:

    def __init__(self):
        # Complexity Time: O(1) for set() and O(log(n)) for get()
        # Complexity Memory: O(m * n)
        self.hash_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map.keys():
            self.hash_map[key] = []
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map.keys(): 
            return ""
        else:
            mood = ""
            values = self.hash_map.get(key, [])
            l, r = 0, len(values) - 1
            while l <= r: 
                m = l + (r - l)//2
                if values[m][0] <= timestamp:
                    mood = values[m][1]
                    l = m + 1
                else: 
                    r = m - 1
            return mood