class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for i in words:
            flag = True
            for j in i:
                if(j not in allowed):
                    flag = False
                    break
            if(flag == True):
                count += 1
        return count