class Solution:
    def numberOfMatches(self, n: int) -> int:
        teamsCompeting = n
        matches = 0

        while teamsCompeting != 1:
            matches += teamsCompeting // 2
            if teamsCompeting % 2 == 0:
                teamsCompeting = teamsCompeting // 2
            else:
                teamsCompeting = (teamsCompeting // 2) + 1

        return matches
