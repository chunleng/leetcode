class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        shortest_len = len(strs[0])
        shortest_index = 0
        for i in range(1, len(strs)):
            if len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
                shortest_index = i

        shortest_word = strs[shortest_index]
        del strs[shortest_index]

        current_prefix = 0
        for i in range(shortest_len):
            for s in strs:
                if s[i] != shortest_word[i]:
                    return shortest_word[0:current_prefix]
            current_prefix += 1
        return shortest_word
