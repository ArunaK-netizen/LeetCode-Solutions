class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)
        for user_id, minute in logs:
            UAM[user_id].add(minute)

        counts = [0] * k
        for minutes in UAM.values():
            if len(minutes) <= k:
                counts[len(minutes) - 1] += 1

        return counts

