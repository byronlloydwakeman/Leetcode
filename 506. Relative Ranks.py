class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ordered_scores = score.copy()
        ordered_scores.sort()
        ordered_scores = ordered_scores[::-1]
        print(ordered_scores)

        # Have an ordered copy 
        # Check index against ordered copy

        for index, cur_score in enumerate(score):
            ord_index = ordered_scores.index(cur_score)
            if ord_index == 0:
                score[index] = "Gold Medal"
            elif ord_index == 1:
                score[index] = "Silver Medal"
            elif ord_index == 2:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(ord_index + 1)

        return score


