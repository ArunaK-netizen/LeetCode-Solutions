class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, pair, score):
            stack = []
            count = 0
            for char in s:
                if stack and stack[-1] + char == pair:
                    stack.pop()
                    count += score
                else:
                    stack.append(char)
            return ''.join(stack), count

        score = 0

        if x >= y:
            s, ab_score = remove_pairs(s, "ab", x)
            score += ab_score
            s, ba_score = remove_pairs(s, "ba", y)
            score += ba_score
        else:
            s, ba_score = remove_pairs(s, "ba", y)
            score += ba_score
            s, ab_score = remove_pairs(s, "ab", x)
            score += ab_score

        return score
