class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_point = len(s) // 2

        return self.find_vowel(s, 0, half_point) == self.find_vowel(
            s, half_point, len(s)
        )

    def find_vowel(self, s: str, start: int, end: int):
        vowel_cnt = 0
        for i in range(start, end):
            if s[i].lower() in "aeiou":
                vowel_cnt += 1
        return vowel_cnt
