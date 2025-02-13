class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        testedCount = 0

        for i in range(len(batteryPercentages)):
            if (batteryPercentages[i] > 0):
                testedCount += 1

                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return testedCount
