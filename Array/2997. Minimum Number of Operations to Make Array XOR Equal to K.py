class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorTotal = 0
        for i in nums:
            xorTotal ^= i

        binary = str(bin(xorTotal)).replace("0b", "")
        k = str(bin(k)).replace("0b", "")
        if (len(k) < len(binary)):
            k = "0" * (len(binary) - len(k)) + k
        elif (len(k) > len(binary)):
            binary = "0" * (len(k) - len(binary)) + binary
        count = 0
        for i in range(len(binary)):
            if (k[i] != binary[i]):
                count += 1
        return count

