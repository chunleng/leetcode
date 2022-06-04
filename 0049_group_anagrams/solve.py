from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for word in strs:
            d[''.join(sorted(word))].append(word)

        return list(d.values())
