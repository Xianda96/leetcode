class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                diff = i - d[s[i]] - 1
                if distance[ord(s[i]) - 97] != diff:
                    return False
        return True
