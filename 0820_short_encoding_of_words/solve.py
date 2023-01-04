from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)

        candidates: List[str] = []
        for word in words:
            is_candidate = True
            for c in candidates:
                if c.endswith(word):
                    is_candidate = False
                    break
            if is_candidate:
                candidates.append(word)

        return sum([len(c) for c in candidates]) + len(candidates)
