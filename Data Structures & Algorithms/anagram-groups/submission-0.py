class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for str in strs:
            s = "".join(sorted(str))
            if s not in data:
                data[s] = []
            data[s].append(str)
        return list(data.values())