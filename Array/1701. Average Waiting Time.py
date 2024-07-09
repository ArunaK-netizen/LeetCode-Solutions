class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTimes = []
        endingTimes = []
        for i in range(len(customers)):
            startingTime = customers[i][0]
            endingTime = customers[i][1] + startingTime

            if (i == 0):
                waitingTimes.append(endingTime - startingTime)
                endingTimes.append(endingTime)

            else:
                if (startingTime < endingTimes[i - 1]):
                    waitingTimes.append(endingTime - startingTime + endingTimes[i - 1] - startingTime)
                    endingTimes.append(endingTimes[i - 1] + customers[i][1])
                else:
                    waitingTimes.append(endingTime - startingTime)
                    endingTimes.append(endingTime)

        return sum(waitingTimes) / len(waitingTimes)

