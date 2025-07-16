class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anag = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in map_anag:
                map_anag[key] = []
            map_anag[key].append(s)
        
        return list(map_anag.values())
        