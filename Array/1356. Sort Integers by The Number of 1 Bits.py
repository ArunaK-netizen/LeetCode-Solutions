class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def calOneBits(num):
            count = 0
            while num != 0:
                num = num & num - 1
                count += 1
            return count

        oneBits = []
        for i in range(len(arr)):
            count = calOneBits(arr[i])
            oneBits.append(count)

        for i in range(len(oneBits)):
            for j in range(i + 1, len(oneBits)):
                if (oneBits[i] < oneBits[j]):
                    oneBits[i], oneBits[j] = oneBits[j], oneBits[i]
                    arr[i], arr[j] = arr[j], arr[i]

                elif (oneBits[i] == oneBits[j] and arr[i] < arr[j]):
                    oneBits[i], oneBits[j] = oneBits[j], oneBits[i]
                    arr[i], arr[j] = arr[j], arr[i]
        return arr[::-1]

