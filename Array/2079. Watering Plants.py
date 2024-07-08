class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        currCapacity = capacity

        for i in range(len(plants) - 1):
            if (currCapacity >= plants[i]):
                currCapacity -= plants[i]
                steps += 1

            if (currCapacity < plants[i + 1]):
                currCapacity = capacity
                steps += (i + 1) + (i + 1)

        return steps + 1