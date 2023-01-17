import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall("\w+", paragraph.lower())
        b = set(banned)
        return collections.Counter(w for w in words if w not in b).most_common(1)[0][0]
