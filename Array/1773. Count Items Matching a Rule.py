class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if (ruleKey == "color"):
            keyIndex = 1
        elif (ruleKey == "type"):
            keyIndex = 0
        else:
            keyIndex = 2

        matches = 0
        for i in range(len(items)):
            if (items[i][keyIndex] == ruleValue):
                matches += 1
        return matches
