class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev = 0
        for i in bank:
            ones = i.count("1")
            if (ones != 0):
                count += prev * ones
                prev = ones
        return count
