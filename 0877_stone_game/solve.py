class Solution:
    dp: dict[tuple[int, int], tuple[int, int]]= {}
    def stoneGame(self, piles: list[int]) -> bool:
        (alice, bob) = self.best_score(True, 0, 0, piles, 0, len(piles)-1)
        return alice > bob

    def best_score(self, is_turn: bool, alice_score: int, bob_score: int, piles: list[int], start: int, end: int) -> tuple[int, int]:
        if end < start:
            return (alice_score, bob_score)

        if (start, end) in self.dp:
            return self.dp[(start, end)]

        if is_turn:
            scores_1 = self.best_score(False, alice_score + piles[start], bob_score, piles, start + 1, end)
            scores_2 = self.best_score(False, alice_score + piles[end], bob_score, piles, start, end - 1)
            scores = scores_1 if scores_1[0] > scores_1[1] else scores_2
        else:
            scores_1 = self.best_score(True, alice_score, bob_score + piles[start], piles, start + 1, end)
            scores_2 = self.best_score(True, alice_score, bob_score + piles[end], piles, start, end - 1)
            scores = scores_1 if scores_1[1] > scores_2[0] else scores_2

        self.dp[(start, end)] = scores
        return scores
