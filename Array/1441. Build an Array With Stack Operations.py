class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = [i for i in range(1, n + 1)]
        operations = []
        current = []
        for i in range(n):

            current.append(stream[i])
            operations.append("Push")
            if (current == target):
                return operations
            if (current[:len(current)] == target[:len(current)]):
                continue
            else:
                current.pop(-1)
                operations.append("Pop")
        return operations

